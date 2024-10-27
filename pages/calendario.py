import requests
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Definir a data de hoje como a data inicial
data_hoje = datetime.today().strftime('%Y-%m-%d')

# Definir a data final como um mês à frente da data de hoje
data_futura = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')

# Definir o número de itens por página
qtd = 100

# Título e descrição da aplicação
st.title("Calendário de Publicações do IBGE")

# Fazer a requisição à API usando a data de hoje e a data final como parâmetros
url = f"https://servicodados.ibge.gov.br/api/v3/calendario/?qtd={qtd}&de={data_hoje}&ate={data_futura}"
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Extrair os itens (dados de divulgação)
    items = data['items']

    # Organizar os dados em uma tabela usando pandas
    df = pd.DataFrame(items, columns=['titulo', 'data_divulgacao'])

    # Converter a coluna 'data_divulgacao' para o formato datetime para ordenação
    df['data_divulgacao'] = pd.to_datetime(df['data_divulgacao'], format='%d/%m/%Y %H:%M:%S')

    # Ordenar os dados pela coluna 'data_divulgacao' de forma crescente
    df = df.sort_values(by='data_divulgacao').reset_index(drop=True)

    # Exibir a tabela no Streamlit
    st.dataframe(df)
else:
    st.error(f"Erro na requisição: {response.status_code}")
