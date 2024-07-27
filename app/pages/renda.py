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
        "fato_classe_social_limite"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

def main():
    global dados
    dados = carregar_dados()

def show_desigualdade_page():
  
    # Supondo que 'dados' é um dicionário com DataFrames, ajuste conforme necessário
    df_fato_classe_social_renda = dados['fato_classe_social_limite']
    
    # Converta a coluna 'Data' para datetime e ordene os dados
    df_fato_classe_social_renda['Data'] = pd.to_datetime(df_fato_classe_social_renda['Data'])
    df_fato_classe_social_renda = df_fato_classe_social_renda.sort_values(by='Data')
    
    fig = go.Figure()
    
    # Adicione traços para cada coluna
    colunas = [
        "Até o P5",
        "Maior que o P5 até o P10",
        "Maior que o P10 até o P20",
        "Maior que o P20 até o P30",
        "Maior que o P30 até o P40",
        "Maior que o P40 até o P50",
        "Maior que o P50 até o P60",
        "Maior que o P60 até o P70",
        "Maior que o P70 até o P80",
        "Maior que o P80 até o P90",
        "Maior que o P90 até o P95",
        "Maior que o P95 até o P99",
        "Maior que o P99"
    ]
    
    cores = [
        'blue', 'green', 'red', 'purple', 'orange', 'pink', 'brown', 
        'gray', 'olive', 'cyan', 'magenta', 'yellow', 'black'
    ]
    
    for coluna, cor in zip(colunas, cores):
        fig.add_trace(go.Scatter(
            x=df_fato_classe_social_renda['Data'],
            y=df_fato_classe_social_renda[coluna],
            name=coluna,
            line=dict(color=cor),
            text=df_fato_classe_social_renda[coluna],
            textposition='top center'
        ))
    
    fig.update_layout(
        title='Desigualdade Social ao Longo do Tempo',
        xaxis_title='Data',
        yaxis_title='Valor',
        legend_title='Percentil',
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
    show_desigualdade_page()