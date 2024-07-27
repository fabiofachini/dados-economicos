import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Energia", layout="wide")
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
        "fato_energia"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_energia_page():
    df_energia = dados['fato_energia']
    df_energia['Data'] = pd.to_datetime(df_energia['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_energia['Data'],
        y=df_energia['Energia_Industrial'],
        name='Industrial',
        line=dict(color='pink'),
        text=df_energia['Energia_Industrial'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_energia['Data'],
        y=df_energia['Energia_Outros'],
        name='Outros',
        line=dict(color='blue'),
        text=df_energia['Energia_Outros'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_energia['Data'],
        y=df_energia['Energia_Residencial'],
        name='Residencial',
        line=dict(color='green'),
        text=df_energia['Energia_Residencial'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_energia['Data'],
        y=df_energia['Energia_Total'],
        name='Total',
        line=dict(color='red'),
        text=df_energia['Energia_Total'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Energia Elétrica',
        xaxis_title='Ano',
        yaxis_title='Consumo de Energia (Kw/h)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_energia_page()