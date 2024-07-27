import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="População", layout="wide")
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
        "fato_populacao_anual"]
    
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
        name='População Anual',
        marker_color='blue',
        text=df_populacao_anual['Populacao_Anual'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Populacao_Anual',
        xaxis_title='Ano',
        yaxis_title='Populacao_Anual',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_pop_page()