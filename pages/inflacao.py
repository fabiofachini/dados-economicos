import streamlit as st
import pandas as pd
import pymssql
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go

# Configurações da página
st.set_page_config(page_title="Inflação", layout="wide")

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
        "int_inflacao_joined",
        "fato_meta_inflacao"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_cambio_page():
    df_inflacao = dados['int_inflacao_joined']
    df_inflacao_meta = dados['fato_meta_inflacao']
    df_inflacao['Data'] = pd.to_datetime(df_inflacao['Data'])

    fig = go.Figure()

    # Adicionando a primeira série de barras para IPCA_Mes
    fig.add_trace(go.Scatter(
        x=df_inflacao['Data'],
        y=df_inflacao['IPCA_Mes'],
        name='IPCA Mensal',
        line=dict(color='#1f77b4'),
        text=df_inflacao['IPCA_Mes'],
        textposition='top center'
    ))

    # Adicionando a segunda série de barras para IPCA_Ano
    fig.add_trace(go.Scatter(
        x=df_inflacao['Data'],
        y=df_inflacao['IPCA_Ano'],
        name='IPCA Anual',
        line=dict(color='#ff7f0e'),
        text=df_inflacao['IPCA_Ano'],
        textposition='top center'
    ))

    # Adicionando a terceira série de barras para IPCA_12M
    fig.add_trace(go.Scatter(
        x=df_inflacao['Data'],
        y=df_inflacao['IPCA_12M'],
        name='IPCA 12 Meses',
        line=dict(color='#2ca02c'),
        text=df_inflacao['IPCA_12M'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_inflacao_meta['Data'],
        y=df_inflacao_meta['Meta_Inflacao'],
        name='Meta Inflação',
        line=dict(color='black'),
        text=df_inflacao_meta['Meta_Inflacao'],
        textposition='top center'
    ))

    fig.update_layout(
        title='IPCA - Variação mensal, acumulada no ano, acumulada em 12 meses e meta anual - Fonte: IBGE',
        xaxis_title='Data',
        yaxis_title='Variação (%)',
        barmode='group',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########

    df_inflacao_inpc = dados['int_inflacao_joined']
    df_inflacao_inpc['Data'] = pd.to_datetime(df_inflacao_inpc['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_inflacao_inpc['Data'],
        y=df_inflacao_inpc['INPC_Mes'],
        name='INPC Mensal',
        line=dict(color='#1f77b4'),
        text=df_inflacao_inpc['INPC_Mes'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_inflacao_inpc['Data'],
        y=df_inflacao_inpc['INPC_Ano'],
        name='INPC Anual',
        line=dict(color='#ff7f0e'),
        text=df_inflacao_inpc['INPC_Ano'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_inflacao_inpc['Data'],
        y=df_inflacao_inpc['INPC_12M'],
        name='INPC 12 Meses',
        line=dict(color='#2ca02c'),
        text=df_inflacao_inpc['INPC_12M'],
        textposition='top center'
    ))

    fig.update_layout(
        title='INPC - Variação mensal, acumulada no ano, acumulada em 12 meses e meta anual - Fonte: IBGE',
        xaxis_title='Data',
        yaxis_title='Variação (%)',
        barmode='group',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########

    df_inflacao_igpm = dados['int_inflacao_joined']
    df_inflacao_igpm['Data'] = pd.to_datetime(df_inflacao_igpm['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_inflacao_igpm['Data'],
        y=df_inflacao_igpm['IGPM_Mes'],
        name='IGPM Mensal',
        line=dict(color='#1f77b4'),
        text=df_inflacao_igpm['IGPM_Mes'],
        textposition='top center'
    ))

    fig.update_layout(
        title='IGP-M - Variação mensal - Fonte: BACEN',
        xaxis_title='Data',
        yaxis_title='Variação (%)',
        barmode='group',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
    show_cambio_page()