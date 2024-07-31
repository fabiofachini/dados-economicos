import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Renda", layout="wide")
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
        "stg_ibge__limites_classe_social",
        "fato_rendimento_atividade",
        "fato_rendimento_posicao",
        "fato_gini",
        "fato_endividamento",
        "stg_ibge__rendimento_todos_os_trabalhos",
        "stg_ibge__massa_salarial_habitualmente"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_desigualdade_page():
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
        title='Limites das Classes Sociais: Percentil',
        xaxis_title='Classes Sociais',
        yaxis_title='Renda R$',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

#########
    # Supondo que 'dados' é um dicionário com DataFrames, ajuste conforme necessário
    df_rendimento_atividade = dados['fato_rendimento_atividade']
    
    # Converta a coluna 'Data' para datetime e ordene os dados
    df_rendimento_atividade['Data'] = pd.to_datetime(df_rendimento_atividade['Data'])
    df_rendimento_atividade = df_rendimento_atividade.sort_values(by='Data')
    
    fig = go.Figure()

    categorias = [
        'Agricultura', 'Indústria', 'Construção', 'Comércio', 'Transporte', 
        'Alojamento', 'Informação, Comunic., Financ., Adm.', 
        'Administração Pública, Saúde, Educação', 'Outros Serviços', 
        'Serviços Domésticos', 'Total'
    ]
    
    cores = [
        'blue', 'green', 'red', 'purple', 'orange', 
        'pink', 'brown', 'gray', 'olive', 'cyan', 'magenta'
    ]
    
    for categoria, cor in zip(categorias, cores):
        fig.add_trace(go.Scatter(
            x=df_rendimento_atividade['Data'],
            y=df_rendimento_atividade[categoria],
            mode='lines',
            name=categoria,
            line=dict(color=cor),
            text=df_rendimento_atividade[categoria],
            textposition='top center'
        ))

    fig.update_layout(
        title='Rendimento Real por Atividade',
        xaxis_title='Data',
        yaxis_title='Rendimento (R$)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

#########
    # Supondo que 'dados' é um dicionário com DataFrames, ajuste conforme necessário
    df_rendimento_posicao = dados['fato_rendimento_posicao']
    
    # Converta a coluna 'Data' para datetime e ordene os dados
    df_rendimento_posicao['Data'] = pd.to_datetime(df_rendimento_posicao['Data'])
    df_rendimento_posicao = df_rendimento_posicao.sort_values(by='Data')
    
    fig = go.Figure()

    categorias = [
        'Conta própria', 'Empregado', 'Empregado no setor público', 'Empregador', 
        'Total']
    
    cores = [
        'blue', 'green', 'red', 'purple', 'orange']
    
    for categoria, cor in zip(categorias, cores):
        fig.add_trace(go.Scatter(
            x=df_rendimento_posicao['Data'],
            y=df_rendimento_posicao[categoria],
            mode='lines',
            name=categoria,
            line=dict(color=cor),
            text=df_rendimento_posicao[categoria],
            textposition='top center'
        ))

    fig.update_layout(
        title='Rendimento Real por Posição',
        xaxis_title='Data',
        yaxis_title='Rendimento (R$)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

##########

    df_rend_todos = dados['stg_ibge__rendimento_todos_os_trabalhos']
    df_rend_todos['Data'] = pd.to_datetime(df_rend_todos['Data'])
    df_rend_todos = df_rend_todos.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_rend_todos['Data'],
        y=df_rend_todos['Rendimento_Todos_os_Trabalhos'],
        name='Rendimento Mensal Todos os Trabalhos',
        line=dict(color='blue'),
        text=df_rend_todos['Rendimento_Todos_os_Trabalhos'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Rendimento Mensal Todos os Trabalhos',
        xaxis_title='Data',
        yaxis_title='Rendimento R$',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########
    df_massa = dados['stg_ibge__massa_salarial_habitualmente']
    df_massa['Data'] = pd.to_datetime(df_massa['Data'])
    df_massa = df_massa.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_massa['Data'],
        y=df_massa['Massa_Salarial_Habitualmente'],
        name='Massa Salarial em Milhões de Reais',
        line=dict(color='blue'),
        text=df_massa['Massa_Salarial_Habitualmente'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Massa Salarial em Milhões de Reais',
        xaxis_title='Data',
        yaxis_title='Rendimento R$',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)
##############

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
        title='Índice de Gini',
        xaxis_title='Ano',
        yaxis_title='Índice',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########

    df_endividamento_f = dados['fato_endividamento']
    df_endividamento_f['Data'] = pd.to_datetime(df_endividamento_f['Data'])
    df_endividamento_f = df_endividamento_f.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_endividamento_f['Data'],
        y=df_endividamento_f['Endividamento_Familias'],
        name='Endividamento',
        line=dict(color='blue'),
        text=df_endividamento_f['Endividamento_Familias'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_endividamento_f['Data'],
        y=df_endividamento_f['Endividamento_Familias_S_Habitacional'],
        name='Endividamento Sem Habitacional',
        line=dict(color='green'),
        text=df_endividamento_f['Endividamento_Familias_S_Habitacional'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Endividamento das Famílias',
        xaxis_title='Data',
        yaxis_title='Taxa (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)
    
if __name__ == "__main__":
    main()
    show_desigualdade_page()