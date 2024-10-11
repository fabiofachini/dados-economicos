import streamlit as st
import pandas as pd
import pymssql
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go

# Configurações da página
st.set_page_config(page_title="Desemprego", layout="wide")

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
        "fato_populacao_forca_trabalho",
        "int_trabalho_joined"]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

@st.cache_data(ttl=85000)
def convert_df(df):
    return df.to_csv().encode("utf-8")

def main():
    global dados
    dados = carregar_dados()

def show_desemprego_page():
    df_desemprego = dados['int_trabalho_joined']
    df_desemprego['Data'] = pd.to_datetime(df_desemprego['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Desalentados'],
        name='Desalentados',
        line=dict(color='blue'),
        text=df_desemprego['Taxa_de_Desalentados'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Desocupacao'],
        name='Desocupação',
        line=dict(color='green'),
        text=df_desemprego['Taxa_de_Desocupacao'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Informalidade'],
        name='Informalidade',
        line=dict(color='purple'),
        text=df_desemprego['Taxa_de_Informalidade'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Part_Forca_de_Trabalho'],
        name='Part. Força de Trabalho',
        line=dict(color='orange'),
        text=df_desemprego['Taxa_de_Part_Forca_de_Trabalho'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Subocupacao'],
        name='Subocupação',
        line=dict(color='brown'),
        text=df_desemprego['Taxa_de_Subocupacao'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Taxas de indicadores de desemprego (%) - Fonte: IBGE',
        xaxis_title='Data',
        yaxis_title='Taxa (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Botão de download
    csv = convert_df(df_desemprego)
    st.download_button(
        label="Download dos dados em CSV",
        data=csv,
        file_name="desemprego.csv",
        mime="text/csv",
        icon=":material/download:")

########

    df_forca_trab = dados['fato_populacao_forca_trabalho']
    df_forca_trab['Data'] = pd.to_datetime(df_forca_trab['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['Forca_Trabalho'],
        name='Força de Trabalho',
        line=dict(color='blue'),
        text=df_forca_trab['Forca_Trabalho'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['Forca_Trabalho_Ocupada'],
        name='Força de Trabalho Ocupada',
        line=dict(color='green'),
        text=df_forca_trab['Forca_Trabalho_Ocupada'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['Forca_Trabalho_Desocupada'],
        name='Força Trabalho Desocupada',
        line=dict(color='purple'),
        text=df_forca_trab['Forca_Trabalho_Desocupada'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['Fora_Forca_Trabalho'],
        name='Fora da Força Trabalho',
        line=dict(color='orange'),
        text=df_forca_trab['Fora_Forca_Trabalho'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['Forca_Trabalho_Total'],
        name='Força Trabalho',
        line=dict(color='brown'),
        text=df_forca_trab['Forca_Trabalho_Total'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_forca_trab['Data'],
        y=df_forca_trab['População_Total'],
        name='População',
        line=dict(color='black'),
        text=df_forca_trab['População_Total'],
        textposition='top center'
    ))


    fig.update_layout(
        title='Indicadores de força de trabalho (mil pessoas) - Fonte: IBGE',
        xaxis_title='Data',
        yaxis_title='População',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Botão de download
    csv = convert_df(df_forca_trab)
    st.download_button(
        label="Download dos dados em CSV",
        data=csv,
        file_name="forca_trabalho.csv",
        mime="text/csv",
        icon=":material/download:")

if __name__ == "__main__":
    main()
    show_desemprego_page()