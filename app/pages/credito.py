import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Crédito", layout="wide")
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
        "int_credito_joined"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_credito_page():
    df_carteira = dados['int_credito_joined']
    df_carteira['Data'] = pd.to_datetime(df_carteira['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_carteira['Data'],
        y=df_carteira['Carteira_de_Credito'],
        name='Carteira_de_Credito',
        line=dict(color='blue'),
        text=df_carteira['Carteira_de_Credito'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_carteira['Data'],
        y=df_carteira['Carteira_de_Credito_PF'],
        name='Carteira_de_Credito_PF',
        line=dict(color='green'),
        text=df_carteira['Carteira_de_Credito_PF'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_carteira['Data'],
        y=df_carteira['Carteira_de_Credito_PJ'],
        name='Carteira_de_Credito_PJ',
        line=dict(color='purple'),
        text=df_carteira['Carteira_de_Credito_PJ'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Carteira_de_Credito',
        xaxis_title='Data',
        yaxis_title='Reais',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

########

    df_concessao = dados['int_credito_joined']
    df_concessao['Data'] = pd.to_datetime(df_concessao['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_concessao['Data'],
        y=df_concessao['Concessao_de_Credito'],
        name='Concessao_de_Credito',
        marker_color='blue',
        text=df_concessao['Concessao_de_Credito'],
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=df_concessao['Data'],
        y=df_concessao['Concessao_de_Credito_PF'],
        name='Concessao_de_Credito_PF',
        marker_color='green',
        text=df_concessao['Concessao_de_Credito_PF'],
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=df_concessao['Data'],
        y=df_concessao['Concessao_de_Credito_PJ'],
        name='Concessao_de_Credito_PJ',
        marker_color='purple',
        text=df_concessao['Concessao_de_Credito_PJ'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Força de Trabalho',
        xaxis_title='Data',
        yaxis_title='População',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_credito_page()