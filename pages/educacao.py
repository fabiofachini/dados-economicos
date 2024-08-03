import streamlit as st
import pandas as pd
import pymssql
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title, hide_pages

# Configurações da página
st.set_page_config(page_title="Educação", layout="wide")
add_page_title()

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
        "fato_analfabetismo",
        "fato_instrucao"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_educacao_page():

    df_instrucao = dados['fato_instrucao']
    df_instrucao['Data'] = pd.to_datetime(df_instrucao['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_instrucao['Data'],
        y=df_instrucao['Sem Instrução'],
        mode='lines+markers',
        name='Sem Instrução',
        line=dict(color='black'),
        text=df_instrucao['Sem Instrução'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_instrucao['Data'],
        y=df_instrucao['Fundamental'],
        mode='lines+markers',
        name='Fundamental',
        line=dict(color='blue'),
        text=df_instrucao['Fundamental'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_instrucao['Data'],
        y=df_instrucao['Médio'],
        mode='lines+markers',
        name='Médio',
        line=dict(color='green'),
        text=df_instrucao['Médio'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_instrucao['Data'],
        y=df_instrucao['Superior'],
        mode='lines+markers',
        name='Superior',
        line=dict(color='red'),
        text=df_instrucao['Superior'],
        textposition='top center'
    ))    

    fig.update_layout(
        title='Pessoas de 14 anos ou mais de idade por nível de instrução - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='População Milhões',
        legend_title='Instrução',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

##########
    df_analfabetismo = dados['fato_analfabetismo']
    df_analfabetismo['Data'] = pd.to_datetime(df_analfabetismo['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Mulheres'],
        mode='lines+markers',
        name='Mulheres',
        line=dict(color='black'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Mulheres'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Homens'],
        mode='lines+markers',
        name='Homens',
        line=dict(color='blue'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Homens'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Total'],
        mode='lines+markers',
        name='Total',
        line=dict(color='green'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Total'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Taxa de analfabetismo das pessoas de 15 anos ou mais de idade - Fonte: IBGE',
        xaxis_title='Ano',
        yaxis_title='Taxa de Analfabetismo (%)',
        legend_title='Sexo',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_educacao_page()