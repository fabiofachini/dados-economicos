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
        "fato_pib_variacao_tri",
        "int_nfsp_joined",
        "stg_bacen__divida_liquida_pib_setor_publico"]
    
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
        name='PIB Anual - variação em volume (%) - Fonte: IBGE',
        marker_color='#262730',
        text=df_pib['PIB_Anual'],
        textposition='auto'
    ))

    fig.update_layout(
        title='PIB Anual - variação em volume (%) - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Variação (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

#############
    df_pib_tri = dados['fato_pib_variacao_tri']
    df_pib_tri['Data'] = pd.to_datetime(df_pib_tri['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_pib_tri['Data'],
        y=df_pib_tri['PIB_Variacao_Trimestral'],
        name='PIB - Taxa trimestre contra trimestre imediatamente anterior (%) - Fonte: IBGE',
        marker_color='red',
        text=df_pib_tri['PIB_Variacao_Trimestral'],
        textposition='auto'
    ))

    fig.update_layout(
        title='PIB - Taxa trimestre contra trimestre imediatamente anterior (%) - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Variação (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

#############

    df_nfsp = dados['int_nfsp_joined']
    df_nfsp['Data'] = pd.to_datetime(df_nfsp['Data'])

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_nfsp['Data'],
        y=df_nfsp['NFSP_PIB_Setor_Publico_Mes'],
        name='Fluxo Mensal',
        marker_color='blue',
        text=df_nfsp['NFSP_PIB_Setor_Publico_Mes'],
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=df_nfsp['Data'],
        y=df_nfsp['NFSP_PIB_Setor_Publico_Ano'],
        name='Fluxo Anual',
        marker_color='green',
        text=df_nfsp['NFSP_PIB_Setor_Publico_Ano'],
        textposition='auto'
    ))

    fig.update_layout(
        title='Resultado primário do setor público consolidado (% PIB) - Fonte: BACEN',
        xaxis_title='Data',
        yaxis_title='Percentual (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

###############

    df_divida_pib = dados['stg_bacen__divida_liquida_pib_setor_publico']
    df_divida_pib['Data'] = pd.to_datetime(df_divida_pib['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_divida_pib['Data'],
        y=df_divida_pib['Divida_Liquida_PIB_Setor_Publico'],
        name='Divida_Liquida_PIB_Setor_Publico',
        line=dict(color='blue'),
        text=df_divida_pib['Divida_Liquida_PIB_Setor_Publico'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Dívida líquida do setor público consolidado (% PIB) - Fonte: BACEN',
        xaxis_title='Data',
        yaxis_title='Percentual (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
    show_pib_page()