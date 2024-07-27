import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="PIB", layout="wide")
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
        "fato_pib_anual_pc",
        "fato_pib_anual",
        "fato_pib_variacao_tri"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_pib_page():
    df_pib = dados['fato_pib_anual']
    df_pib['Data'] = pd.to_datetime(df_pib['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_pib['Data'],
        y=df_pib['PIB_Anual'],
        name='PIB',
        marker_color='LightSkyBlue',
        text=df_pib['PIB_Anual'],
        textposition='auto'
    ))

    fig.update_layout(
        title='PIB: Variação Anual',
        xaxis_title='Ano',
        yaxis_title='Variação (%)',
        legend_title='Categoria',
        plot_bgcolor='rgb(211,211,211)'
    )

    st.plotly_chart(fig, use_container_width=True)

#############
    df_pib_tri = dados['fato_pib_variacao_tri']
    df_pib_tri['Data'] = pd.to_datetime(df_pib_tri['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_pib_tri['Data'],
        y=df_pib_tri['PIB_Variacao_Trimestral'],
        mode='lines+markers',
        name='PIB',
        line=dict(color='LightSeaGreen'),
        text=df_pib_tri['PIB_Variacao_Trimestral'],
        textposition='top center'
    ))

    fig.update_layout(
        title='PIB Variação Trimestral',
        xaxis_title='Ano',
        yaxis_title='Variação (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

#############
    df_pib_anual_pc = dados['fato_pib_anual_pc']
    df_pib_anual_pc['Data'] = pd.to_datetime(df_pib_anual_pc['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_pib_anual_pc['Data'],
        y=df_pib_anual_pc['PIB_Anual'],
        name='PIB',
        marker_color='blue',
        text=df_pib_anual_pc['PIB_Anual'],
        textposition='auto'
    ))

    fig.update_layout(
        title='PIB_Anual_PC',
        xaxis_title='Ano',
        yaxis_title='PIB',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_pib_page()