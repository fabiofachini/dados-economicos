import requests
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Lista de URLs, descritores e descrições
series = [
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4639/dados', 'tabela': 'NFSP_Governo_Mes', 'descricao': '4639: NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4649/dados', 'tabela': 'NFSP_Setor_Publico_Mes', 'descricao': '4649: NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4782/dados', 'tabela': 'NFSP_Governo_Ano', 'descricao': '4782: NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4792/dados', 'tabela': 'NFSP_Setor_Publico_Ano', 'descricao': '4792: NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5068/dados', 'tabela': 'NFSP_Governo_12m', 'descricao': '5068: NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5078/dados', 'tabela': 'NFSP_Setor_Publico_12m', 'descricao': '5078: NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5354/dados', 'tabela': 'NFSP_PIB_Governo_Mes', 'descricao': '5354: NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5364/dados', 'tabela': 'NFSP_PIB_Setor_Publico_Mes', 'descricao': '5364: NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5497/dados', 'tabela': 'NFSP_PIB_Governo_Ano', 'descricao': '5497: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5507/dados', 'tabela': 'NFSP_PIB_Setor_Publico_Ano', 'descricao': '5507: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5783/dados', 'tabela': 'NFSP_PIB_Governo_12m', 'descricao': '5783: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados', 'tabela': 'NFSP_PIB_Setor_Publico_12m', 'descricao': '5793: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4503/dados', 'tabela': 'Divida_Liquida_PIB_Governo', 'descricao': '4503: Dívida Líquida do Setor Público (% PIB) - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4513/dados', 'tabela': 'Divida_Liquida_PIB_Setor_Publico', 'descricao': '4513: Dívida Líquida do Setor Público (% PIB) - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados', 'tabela': 'Taxa_de_Cambio_Euro', 'descricao': '21619: Taxa de câmbio - Livre - Euro (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21623/dados', 'tabela': 'Taxa_de_Cambio_Libra', 'descricao': '21623: Taxa de câmbio - Livre - Libra Esterlina (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados', 'tabela': 'Taxa_de_Cambio_Dolar', 'descricao': '1: Taxa de câmbio - Livre - Dólar Americano (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados', 'tabela': 'Selic_Anualizada', 'descricao': '1178: Taxa de juros - Selic anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4389/dados', 'tabela': 'CDI_Anualizada', 'descricao': '4389: Taxa de juros - CDI anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados', 'tabela': 'Selic_Meta', 'descricao': '432: Taxa de juros - Meta Selic definida pelo Copom', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados', 'tabela': 'IGPM_Mes', 'descricao': '189: Índice geral de preços do mercado (IGP-M)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.13521/dados', 'tabela': 'Meta_Inflacao', 'descricao': '13521: Meta para a inflação', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20539/dados', 'tabela': 'Carteira_de_Credito', 'descricao': '20539: Saldo da carteira de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20540/dados', 'tabela': 'Carteira_de_Credito_PJ', 'descricao': '20540: Saldo da carteira de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20541/dados', 'tabela': 'Carteira_de_Credito_PF', 'descricao': '20541: Saldo da carteira de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20631/dados', 'tabela': 'Concessao_de_Credito', 'descricao': '20631: Concessões de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20632/dados', 'tabela': 'Concessao_de_Credito_PJ', 'descricao': '20632: Concessões de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20633/dados', 'tabela': 'Concessao_de_Credito_PF', 'descricao': '20633: Concessões de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados', 'tabela': 'Endividamento_Familias', 'descricao': '29037: Endividamento das famílias com o Sistema Financeiro Nacional em relação à renda acumulada dos últimos doze meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29038/dados', 'tabela': 'Envidadamento_Familias_s_Habitacional', 'descricao': '29038: Endividamento das famílias com o Sistema Financeiro Nacional exceto crédito habitacional em relação à renda acumulada dos últimos 12 meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4393/dados', 'tabela': 'Confianca_Consumidor', 'descricao': '4393: Índice de Confiança do Consumidor', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7341/dados', 'tabela': 'Confianca_Industrial', 'descricao': '7341: Índice de Confiança do Empresário Industrial (ICEI) - Geral', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.17660/dados', 'tabela': 'Confianca_Servicos', 'descricao': '17660: Sondagem de Serviços - Índice de Confiança de Serviços', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1402/dados', 'tabela': 'Energia_Comercial', 'descricao': '1402: Consumo de energia elétrica - Brasil - Comercial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1403/dados', 'tabela': 'Energia_Residencial', 'descricao': '1403: Consumo de energia elétrica - Brasil - Residencial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1404/dados', 'tabela': 'Energia_Industrial', 'descricao': '1404: Consumo de energia elétrica - Brasil - Industrial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1405/dados', 'tabela': 'Energia_Outros', 'descricao': '1405: Consumo de energia elétrica - Brasil - Outros', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1406/dados', 'tabela': 'Energia_Total', 'descricao': '1406: Consumo de energia elétrica - Brasil - Total', 'unidade':'GWh', 'periodicidade': 'M'}
]

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# Criar a conexão com o banco de dados
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC Driver 18 for SQL Server"
engine = create_engine(conn_str)

# Loop pelas séries para fazer as requisições e salvar no banco de dados
for serie in series:
    params = {'formato': 'json'}
    response = requests.get(serie['url'], params=params)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        # Inserir dados no banco de dados
        df.to_sql(serie['tabela'], engine, if_exists='replace', index=False, schema='dbo')
        print(f"Dados da série {serie['tabela']} salvos com sucesso no banco de dados.")
        
    else:
        print(f"Falha ao obter dados da série {serie['tabela']}. Status code: {response.status_code}")
print("Fim das importações de dados do BACEN.")