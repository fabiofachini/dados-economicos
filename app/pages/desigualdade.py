import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Desigualdade", layout="wide")
add_page_title()

# Atualize o caminho para o arquivo .env
load_dotenv()

# Função para conectar ao Azure SQL Database
def connect_to_db():
    retries = 5
    delay = 10  # segundos
    for i in range(retries):
        try:
            connection = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                f'SERVER={os.getenv("DB_SERVER")};'
                f'DATABASE={os.getenv("DB_DATABASE")};'
                f'UID={os.getenv("DB_USERNAME")};'
                f'PWD={os.getenv("DB_PASSWORD")}'
            )
            print("Conexão bem-sucedida")
            return connection
        except pyodbc.Error as e:
            print(f"Tentativa {i+1} falhou: {e}")
            if i < retries - 1:
                print(f"Tentando novamente em {delay} segundos...")
                time.sleep(delay)
            else:
                raise

# Função para obter dados de uma tabela específica
@st.cache_data(ttl=85000)
def get_data(table_name):
    conn = connect_to_db()
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Função para carregar todos os dados e armazenar em cache
@st.cache_data(ttl=85000)
def carregar_dados():
    tabelas = [
        "fato_classe_social_renda",
        "fato_classe_social_massa",
        "fato_classe_social_pop",
        "fato_gini",
        "stg_ibge__limites_classe_social"]

    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_desigualdade_page():
    df_renda = dados['fato_classe_social_renda']

    # Convertendo a coluna Data para o ano (separando apenas o ano para facilitar o plot)
    df_renda['Ano'] = pd.to_datetime(df_renda['Data']).dt.year

    fig = go.Figure()

    # Adicionando as linhas para cada faixa de renda
    for coluna in df_renda.columns[1:-1]:  # Ignorar a primeira coluna (Data) e última (Maior que o P99)
        fig.add_trace(go.Scatter(
            x=df_renda['Ano'],
            y=df_renda[coluna],
            mode='lines+markers',
            name=coluna
        ))

    fig.update_layout(
        title='Rendimento médio mensal real domiciliar per capita, a preços médios do ano (Reais) - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Rendimento (R$)',
        legend_title='Faixas de Renda',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)
    
###########

    df_pop = dados['fato_classe_social_pop']

    # Convertendo a coluna Data para o ano (separando apenas o ano para facilitar o plot)
    df_pop['Ano'] = pd.to_datetime(df_pop['Data']).dt.year

    fig = go.Figure()

    # Adicionando as linhas para cada faixa de renda
    for coluna in df_pop.columns[1:-1]:  # Ignorar a primeira coluna (Data) e última (Maior que o P99)
        fig.add_trace(go.Scatter(
            x=df_pop['Ano'],
            y=df_pop[coluna],
            mode='lines+markers',
            name=coluna
        ))

    fig.update_layout(
        title='População por classes sociais por rendimento domiciliar per capita - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='População',
        legend_title='Classes sociais',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

###########

    df_massa = dados['fato_classe_social_massa']

    # Convertendo a coluna Data para o ano (separando apenas o ano para facilitar o plot)
    df_massa['Ano'] = pd.to_datetime(df_massa['Data']).dt.year

    fig = go.Figure()

    # Adicionando as linhas para cada faixa de renda
    for coluna in df_massa.columns[1:-1]:  # Ignorar a primeira coluna (Data) e última (Maior que o P99)
        fig.add_trace(go.Scatter(
            x=df_massa['Ano'],
            y=df_massa[coluna],
            mode='lines+markers',
            name=coluna
        ))

    fig.update_layout(
        title='Distribuição da massa de rendimento mensal real domiciliar per capita - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Massa salarial (%)',
        legend_title='Classes sociais',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

###########

    df_limite_classe_social = dados['stg_ibge__limites_classe_social']

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_limite_classe_social['Classes_Sociais_Percentil'],
        y=df_limite_classe_social['Limites_Classe_Social'],
        marker_color='#262730',
        text=df_limite_classe_social['Limites_Classe_Social'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Limites superiores das classes de percentual das pessoas (R$) - Fonte: IBGE',
        xaxis_title='Classes Sociais',
        yaxis_title='Reais (R$)',
        legend_title='Classes sociais',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

#############


    df_gini = dados['fato_gini']
    df_gini['Data'] = pd.to_datetime(df_gini['Data'])
    df_gini = df_gini.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_gini['Data'],
        y=df_gini['Indice_de_Gini'],
        name='Índice de Gini',
        line=dict(color='#262730'),
        text=df_gini['Indice_de_Gini'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Índice de Gini - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Índice',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##############


if __name__ == "__main__":
    main()
    show_desigualdade_page()