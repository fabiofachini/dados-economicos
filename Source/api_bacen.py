import requests
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Lista de URLs, descritores e descrições
series = [
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4639/dados', 'tabela': '4639', 'descricao': 'NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4649/dados', 'tabela': '4649', 'descricao': 'NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4782/dados', 'tabela': '4782', 'descricao': 'NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4792/dados', 'tabela': '4792', 'descricao': 'NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5068/dados', 'tabela': '5068', 'descricao': 'NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5078/dados', 'tabela': '5078', 'descricao': 'NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5354/dados', 'tabela': '5354', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5364/dados', 'tabela': '5364', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5497/dados', 'tabela': '5497', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5507/dados', 'tabela': '5507', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5783/dados', 'tabela': '5783', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados', 'tabela': '5793', 'descricao': 'NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4503/dados', 'tabela': '4503', 'descricao': 'Dívida Líquida do Setor Público (% PIB) - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4513/dados', 'tabela': '4513', 'descricao': 'Dívida Líquida do Setor Público (% PIB) - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados', 'tabela': '21619', 'descricao': 'Taxa de câmbio - Livre - Euro (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21623/dados', 'tabela': '21623', 'descricao': 'Taxa de câmbio - Livre - Libra Esterlina (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados', 'tabela': '1', 'descricao': 'Taxa de câmbio - Livre - Dólar Americano (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados', 'tabela': '1178', 'descricao': 'Taxa de juros - Selic anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4389/dados', 'tabela': '4389', 'descricao': 'Taxa de juros - CDI anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados', 'tabela': '432', 'descricao': 'Taxa de juros - Meta Selic definida pelo Copom', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados', 'tabela': '189', 'descricao': 'Índice geral de preços do mercado (IGP-M)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.13521/dados', 'tabela': '13521', 'descricao': 'Meta para a inflação', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1419/dados', 'tabela': '1419', 'descricao': 'IPCA - Variação mensal, acumulada no ano, acumulada em 12 meses e peso mensal, para o índice geral, grupos, subgrupos, itens e subitens de produtos e serviços (de janeiro/2012 até dezembro/2019)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7060/dados', 'tabela': '7060', 'descricao': 'IPCA - Variação mensal, acumulada no ano, acumulada em 12 meses e peso mensal, para o índice geral, grupos, subgrupos, itens e subitens de produtos e serviços (a partir de janeiro/2020)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1100/dados', 'tabela': '1100', 'descricao': 'INPC - Variação mensal, acumulada no ano, acumulada em 12 meses e peso mensal, para o índice geral, grupos, subgrupos, itens e subitens de produtos e serviços (de janeiro/2012 até dezembro/2019)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7063/dados', 'tabela': '7060', 'descricao': 'INPC - Variação mensal, acumulada no ano, acumulada em 12 meses e peso mensal, para o índice geral, grupos, subgrupos, itens e subitens de produtos e serviços (a partir de janeiro/2020)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20539/dados', 'tabela': '20539', 'descricao': 'Saldo da carteira de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20540/dados', 'tabela': '20540', 'descricao': 'Saldo da carteira de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20541/dados', 'tabela': '20541', 'descricao': 'Saldo da carteira de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20631/dados', 'tabela': '20631', 'descricao': 'Concessões de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20632/dados', 'tabela': '20632', 'descricao': 'Concessões de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20633/dados', 'tabela': '20633', 'descricao': 'Concessões de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados', 'tabela': '29037', 'descricao': 'Endividamento das famílias com o Sistema Financeiro Nacional em relação à renda acumulada dos últimos doze meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29038/dados', 'tabela': '29038', 'descricao': 'Endividamento das famílias com o Sistema Financeiro Nacional exceto crédito habitacional em relação à renda acumulada dos últimos 12 meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4393/dados', 'tabela': '4393', 'descricao': 'Índice de Confiança do Consumidor', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7341/dados', 'tabela': '7341', 'descricao': 'Índice de Confiança do Empresário Industrial (ICEI) - Geral', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.17660/dados', 'tabela': '17660', 'descricao': 'Sondagem de Serviços - Índice de Confiança de Serviços', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1402/dados', 'tabela': '1402', 'descricao': 'Consumo de energia elétrica - Brasil - Comercial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1403/dados', 'tabela': '1403', 'descricao': 'Consumo de energia elétrica - Brasil - Residencial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1404/dados', 'tabela': '1404', 'descricao': 'Consumo de energia elétrica - Brasil - Industrial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1405/dados', 'tabela': '1405', 'descricao': 'Consumo de energia elétrica - Brasil - Outros', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1406/dados', 'tabela': '1406', 'descricao': 'Consumo de energia elétrica - Brasil - Total', 'unidade':'GWh', 'periodicidade': 'M'}
]

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# Criar a conexão com o banco de dados
conn_str = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC Driver 17 for SQL Server"
engine = create_engine(conn_str)

# Loop pelas séries para fazer as requisições e salvar no banco de dados
for serie in series:
    params = {'formato': 'json'}
    response = requests.get(serie['url'], params=params)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['descricao'] = serie['descricao']
        df['unidade'] = serie['unidade']
        df['periodicidade'] = serie['periodicidade']
        
        # Inserir dados no banco de dados
        df.to_sql(serie['tabela'], engine, if_exists='replace', index=False, schema='dbo')
        print(f"Dados da série {serie['tabela']} salvos com sucesso no banco de dados.")
        print("Fim das importações de dados do BACEN.")
    else:
        print(f"Falha ao obter dados da série {serie['tabela']}. Status code: {response.status_code}")

