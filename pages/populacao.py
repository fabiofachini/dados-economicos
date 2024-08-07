import streamlit as st
import pandas as pd
import pymssql
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go

# Configurações da página
st.set_page_config(page_title="População", layout="wide")

# Atualize o caminho para o arquivo .env
load_dotenv()

# Função para conectar ao Azure SQL Database
def connect_to_db():
    retries = 5
    delay = 10  # segundos
    for i in range(retries):
        try:
            connection = pymssql.connect(
                server=os.getenv("DB_SERVER"),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE")
            )
            print("Conexão bem-sucedida")
            return connection
        except pymssql.DatabaseError as e:
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
        "fato_populacao_anual",
        "fato_piramide_etaria",
        "stg_ibge__populacao_mensal"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_pop_page():
    df_populacao_anual = dados['fato_populacao_anual']
    df_populacao_anual['Data'] = pd.to_datetime(df_populacao_anual['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_populacao_anual['Data'],
        y=df_populacao_anual['Populacao_Anual'],
        marker_color='#262730',
        text=df_populacao_anual['Populacao_Anual'],
        textposition='auto'
    ))

    fig.update_layout(
        title='População Anual (Mil pessoas) - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='População',
        yaxis=dict(range=[190000, df_populacao_anual['Populacao_Anual'].max() + 5000]),
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

############

    df_populacao_mensal = dados['stg_ibge__populacao_mensal']
    df_populacao_mensal['Data'] = pd.to_datetime(df_populacao_mensal['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_populacao_mensal['Data'],
        y=df_populacao_mensal['Populacao'],
        marker_color='grey',
        text=df_populacao_mensal['Populacao'],
        textposition='auto'
    ))

    fig.update_layout(
        title='População Mensal (Mil pessoas) - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='População',
        yaxis=dict(range=[190000, df_populacao_mensal['Populacao'].max() + 5000]),
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########

    df_piramide_etaria = dados['fato_piramide_etaria']

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_piramide_etaria['Grupo de idade'],
        y=df_piramide_etaria['piramide_etaria'],
        marker_color='#262730',
        text=df_piramide_etaria['piramide_etaria'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Distribuição percentual da população segundo grupos de idade (%) - Pirâmide Etária - Fonte: IBGE',
        xaxis_title='Idade',
        yaxis_title='Percentual da População (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_pop_page()