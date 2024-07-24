import streamlit as st
import pandas as pd
import pyodbc
import os
import time
from dotenv import load_dotenv
import plotly.graph_objects as go

# Atualize o caminho para o arquivo .env
load_dotenv()

# Função para conectar ao Azure SQL Database
def connect_to_db():
    retries = 5
    delay = 20  # segundos
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
@st.cache_data(ttl=86400)  # Cache de 24 horas (86400 segundos)
def get_data(table_name):
    conn = connect_to_db()
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, conn)
    conn.close()
    return data

# Função para carregar todos os dados e armazenar em cache
@st.cache_data(ttl=86400)  # Cache de 24 horas (86400 segundos)
def carregar_dados():
    tabelas = [
        'fato_cambio', 'fato_confianca', 'fato_contas_publicas', 'fato_analfabetismo',
        'fato_instrucao', 'fato_energia', 'fato_inflacao', 'fato_meta_inflacao',
        'fato_juros', 'fato_pib_anual', 'fato_pib', 'fato_piramide_etaria',
        'fato_populacao_anual', 'fato_populacao_forca_trabalho', 'fato_classe_social_limites',
        'fato_classe_social', 'fato_endividamento', 'fato_gini', 'fato_rendimento_atividade',
        'fato_rendimento_posicao', 'fato_rendimento', 'fato_trabalho'
    ]
    
    dados = {tabela: get_data(tabela) for tabela in tabelas}
    return dados

# Função principal
def main():
    global dados
    dados = carregar_dados()
    st.sidebar.title("Selecione um Tema")

    # Opções de navegação
    option = st.sidebar.radio(
        "Escolha uma opção:",
        ["EDUCAÇÃO", "DESIGUALDADE", "DESEMPREGO", "JUROS","CONFIANÇA", "CÂMBIO", "ENERGIA"]
    )

    # Exibir o conteúdo baseado na seleção do usuário
    if option == "EDUCAÇÃO":
        show_educacao_page()
    elif option == "CONFIANÇA":
        show_confianca_page()
    elif option == "ENERGIA":
        show_energia_page()
    elif option == "DESEMPREGO":
        show_desemprego_page()
    elif option == "JUROS":
        show_juros_page()
    elif option == "DESIGUALDADE":
        show_desigualdade_page()
    elif option == "CÂMBIO":
        show_cambio_page()

############################## EDUCAÇÃO #####################################

def show_educacao_page():
    st.title("Educação")
    df_analfabetismo = dados['fato_analfabetismo']
    df_analfabetismo['Data'] = pd.to_datetime(df_analfabetismo['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Mulheres'],
        mode='lines+markers+text',
        name='Mulheres',
        line=dict(color='pink'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Mulheres'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Homens'],
        mode='lines+markers+text',
        name='Homens',
        line=dict(color='blue'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Homens'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_analfabetismo['Data'],
        y=df_analfabetismo['Taxa_de_Analfabetismo_Total'],
        mode='lines+markers+text',
        name='Total',
        line=dict(color='green'),
        text=df_analfabetismo['Taxa_de_Analfabetismo_Total'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Analfabetismo',
        xaxis_title='Ano',
        yaxis_title='Taxa de Analfabetismo (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)


############################## CAMBIO #####################################

def show_cambio_page():
    st.title("Taxas de Câmbio")
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
        title='Taxa de Câmbio',
        xaxis_title='Data',
        yaxis_title='Taxa de Câmbio (R$)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

############################## ENERGIA #####################################

def show_energia_page():
    st.title("Energia Elétrica")
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

############################## JUROS #####################################

def show_juros_page():
    st.title("Taxa de Juros")
    df_juros = dados['fato_juros']
    df_juros['Data'] = pd.to_datetime(df_juros['Data'])
    df_juros = df_juros.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_juros['Data'],
        y=df_juros['Selic_Anualizada'],
        name='Selic Anualizada',
        line=dict(color='green'),
        text=df_juros['Selic_Anualizada'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Taxas de Juros',
        xaxis_title='Ano',
        yaxis_title='Taxa (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

############################## DESEMPREGO #####################################

def show_desemprego_page():
    st.title("Desemprego")
    df_desemprego = dados['fato_trabalho']
    df_desemprego['Data'] = pd.to_datetime(df_desemprego['Data'])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Desalentados'],
        name='Taxa de Desalentados',
        line=dict(color='blue'),
        text=df_desemprego['Taxa_de_Desalentados'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Desocupacao'],
        name='Taxa de Desocupação',
        line=dict(color='green'),
        text=df_desemprego['Taxa_de_Desocupacao'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Informalidade'],
        name='Taxa de Informalidade',
        line=dict(color='purple'),
        text=df_desemprego['Taxa_de_Informalidade'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Part_Forca_de_Trabalho'],
        name='Taxa de Participação da Força de Trabalho',
        line=dict(color='orange'),
        text=df_desemprego['Taxa_de_Part_Forca_de_Trabalho'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_desemprego['Data'],
        y=df_desemprego['Taxa_de_Subocupacao'],
        name='Taxa de Subocupação',
        line=dict(color='brown'),
        text=df_desemprego['Taxa_de_Subocupacao'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Taxas de Desemprego',
        xaxis_title='Data',
        yaxis_title='Taxa (%)',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)

############################## CONFIANÇA #####################################

def show_confianca_page():
    st.title("Confiança")
    df_confianca = dados['fato_confianca']
    df_confianca['Data'] = pd.to_datetime(df_confianca['Data'])
    df_confianca = df_confianca.sort_values(by='Data')

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Industrial'],
        name='Confiança Industrial',
        line=dict(color='blue'),
        text=df_confianca['Confianca_Industrial'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Consumidor'],
        name='Confiança do Consumidor',
        line=dict(color='green'),
        text=df_confianca['Confianca_Consumidor'],
        textposition='top center'
    ))

    fig.add_trace(go.Scatter(
        x=df_confianca['Data'],
        y=df_confianca['Confianca_Servicos'],
        name='Confiança em Serviços',
        line=dict(color='red'),
        text=df_confianca['Confianca_Servicos'],
        textposition='top center'
    ))

    fig.update_layout(
        title='Índices de Confiança',
        xaxis_title='Data',
        yaxis_title='Índice',
        legend_title='Categoria',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)


############################## DESIGUALDADE #####################################

def show_desigualdade_page():
    st.title("Desigualdade de Renda")
    df_desigualdade = dados['fato_classe_social_limites']
    df_desigualdade['Data'] = pd.to_datetime(df_desigualdade['Data'])

    
    # Preencher valores nulos com zero para evitar problemas ao plotar
    df_desigualdade['Limites_Classe_Social'] = df_desigualdade['Limites_Classe_Social'].fillna(0)

    # Separar os dados por percentis para plotar
    percentis = df_desigualdade['Classes_Sociais_Percentil'].unique()

    fig = go.Figure()

    for percentil in percentis:
        df_percentil = df_desigualdade[df_desigualdade['Classes_Sociais_Percentil'] == percentil]
        fig.add_trace(go.Scatter(
            x=df_percentil['Data'],
            y=df_percentil['Limites_Classe_Social'],
            name=f'Classes_Sociais_Percentil {percentil}',
            mode='lines+markers'
        ))

    fig.update_layout(
        title='Desigualdade Econômica por Percentil',
        xaxis_title='Data',
        yaxis_title='Limites_Classe_Social',
        legend_title='Percentil',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig, use_container_width=True)
#___________________________
  

if __name__ == "__main__":
    main()