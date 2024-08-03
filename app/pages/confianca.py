import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Confiança", layout="wide")
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
        "fato_confianca"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_confianca_page():
    df_confianca = dados['fato_confianca']
    df_confianca['Data'] = pd.to_datetime(df_confianca['Data'])
    df_confianca = df_confianca.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Industrial'],
        name='Confiança Industrial (CNI)',
        line=dict(color='blue'),
        text=df_confianca['Confianca_Industrial'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Consumidor'],
        name='Confiança Consumidor (Fecomércio)',
        line=dict(color='green'),
        text=df_confianca['Confianca_Consumidor'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Servicos'],
        name='Confiança Serviços (FGV)',
        line=dict(color='red'),
        text=df_confianca['Confianca_Servicos'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Índice de Confiança da Indústria, Serviços e Consumidor - Fonte: BACEN',
        xaxis_title='Data',
        yaxis_title='Índice',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
    show_confianca_page()