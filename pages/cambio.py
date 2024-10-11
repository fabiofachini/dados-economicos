import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go
import urllib

# Configurações da página
st.set_page_config(page_title="Taxas de Câmbio", layout="wide")

# Atualize o caminho para o arquivo .env
load_dotenv()

# Função para conectar ao Azure SQL Database usando SQLAlchemy
def connect_to_db():
    retries = 5
    delay = 10  # segundos
    for i in range(retries):
        try:
            # Carregar variáveis de ambiente
            server = os.getenv("DB_SERVER")
            database = os.getenv("DB_DATABASE")
            username = os.getenv("DB_USERNAME")
            password = os.getenv("DB_PASSWORD")

            # Criar a string de conexão
            params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}")
            connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

            # Criar o engine de conexão
            engine = create_engine(connection_string)
            print("Conexão bem-sucedida")
            return engine
        except Exception as e:
            print(f"Tentativa {i + 1} falhou: {e}")
            if i < retries - 1:
                print(f"Tentando novamente em {delay} segundos...")
                time.sleep(delay)
            else:
                raise

# Função para obter dados de uma tabela específica
@st.cache_data(ttl=85000)
def get_data(table_name):
    engine = connect_to_db()
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, engine)
    return data

# Função para carregar todos os dados e armazenar em cache
@st.cache_data(ttl=85000)
def carregar_dados():
    tabelas = [
        "fato_cambio"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

@st.cache_data(ttl=85000)
def convert_df(df):
    return df.to_csv().encode("utf-8")

def main():
    global dados
    dados = carregar_dados()

def show_cambio_page():
    df_cambio = dados['fato_cambio']
    df_cambio['Data'] = pd.to_datetime(df_cambio['Data'])
    df_cambio = df_cambio.sort_values(by='Data')
    

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_cambio['Data'],
        y=df_cambio['Taxa_de_Cambio_Dolar'],
        name='Dólar',
        line=dict(color='red'),
        text=df_cambio['Taxa_de_Cambio_Dolar'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_cambio['Data'],
        y=df_cambio['Taxa_de_Cambio_Euro'],
        name='Euro',
        line=dict(color='blue'),
        text=df_cambio['Taxa_de_Cambio_Euro'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_cambio['Data'],
        y=df_cambio['Taxa_de_Cambio_Libra'],
        name='Libra',
        line=dict(color='green'),
        text=df_cambio['Taxa_de_Cambio_Libra'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Taxa de Câmbio (venda) - Fonte: BACEN',
        xaxis_title='Data',
        yaxis_title='Reais (R$)',
        legend_title='Moeda',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Botão de download
    csv = convert_df(df_cambio)
    st.download_button(
        label="Download dos dados em CSV",
        data=csv,
        file_name="cambio.csv",
        mime="text/csv",
        icon=":material/download:")

if __name__ == "__main__":
    main()
    show_cambio_page()