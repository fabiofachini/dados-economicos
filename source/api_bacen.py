import requests
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from time import sleep

# Lista de URLs, descritores e descrições
series = [
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4639/dados', 'tabela': 'nfsp_governo_mes', 'descricao': '4639: NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4649/dados', 'tabela': 'nfsp_setor_publico_mes', 'descricao': '4649: NFSP sem desvalorização cambial - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4782/dados', 'tabela': 'nfsp_governo_ano', 'descricao': '4782: NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4792/dados', 'tabela': 'nfsp_setor_publico_ano', 'descricao': '4792: NFSP sem desvalorização cambial - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5068/dados', 'tabela': 'nfsp_governo_12m', 'descricao': '5068: NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5078/dados', 'tabela': 'nfsp_setor_publico_12m', 'descricao': '5078: NFSP sem desvalorização cambial - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5354/dados', 'tabela': 'nfsp_pib_governo_mes', 'descricao': '5354: NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5364/dados', 'tabela': 'nfsp_pib_setor_publico_mes', 'descricao': '5364: NFSP sem desvalorização cambial (% PIB) - Fluxo mensal corrente - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5497/dados', 'tabela': 'nfsp_pib_governo_ano', 'descricao': '5497: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5507/dados', 'tabela': 'nfsp_pib_setor_publico_ano', 'descricao': '5507: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado no ano - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5783/dados', 'tabela': 'nfsp_pib_governo_12m', 'descricao': '5783: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados', 'tabela': 'nfsp_pib_setor_publico_12m', 'descricao': '5793: NFSP sem desvalorização cambial (% PIB) - Fluxo acumulado em 12 meses - Resultado primário - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4503/dados', 'tabela': 'divida_liquida_pib_governo', 'descricao': '4503: Dívida Líquida do Setor Público (% PIB) - Total - Governo Federal e Banco Central', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4513/dados', 'tabela': 'divida_liquida_pib_setor_publico', 'descricao': '4513: Dívida Líquida do Setor Público (% PIB) - Total - Setor público consolidado', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21619/dados', 'tabela': 'taxa_de_cambio_euro', 'descricao': '21619: Taxa de câmbio - Livre - Euro (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.21623/dados', 'tabela': 'taxa_de_cambio_libra', 'descricao': '21623: Taxa de câmbio - Livre - Libra Esterlina (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados', 'tabela': 'taxa_de_cambio_dolar', 'descricao': '1: Taxa de câmbio - Livre - Dólar Americano (venda)', 'unidade':'R$ u.m.c.', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados', 'tabela': 'selic_anualizada', 'descricao': '1178: Taxa de juros - Selic anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4389/dados', 'tabela': 'cdi_anualizada', 'descricao': '4389: Taxa de juros - CDI anualizada base 252', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados', 'tabela': 'selic_meta', 'descricao': '432: Taxa de juros - Meta Selic definida pelo Copom', 'unidade':'%', 'periodicidade': 'D'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados', 'tabela': 'igpm_mes', 'descricao': '189: Índice geral de preços do mercado (IGP-M)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.13521/dados', 'tabela': 'meta_inflacao', 'descricao': '13521: Meta para a inflação', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20539/dados', 'tabela': 'carteira_de_credito', 'descricao': '20539: Saldo da carteira de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20540/dados', 'tabela': 'carteira_de_credito_pj', 'descricao': '20540: Saldo da carteira de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20541/dados', 'tabela': 'carteira_de_credito_pf', 'descricao': '20541: Saldo da carteira de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20631/dados', 'tabela': 'concessao_de_credito', 'descricao': '20631: Concessões de crédito - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20632/dados', 'tabela': 'concessao_de_credito_pj', 'descricao': '20632: Concessões de crédito - Pessoas jurídicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.20633/dados', 'tabela': 'concessao_de_credito_pf', 'descricao': '20633: Concessões de crédito - Pessoas físicas - Total', 'unidade':'R$ Milhões', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados', 'tabela': 'endividamento_familias', 'descricao': '29037: Endividamento das famílias com o Sistema Financeiro Nacional em relação à renda acumulada dos últimos doze meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.29038/dados', 'tabela': 'endividamento_familias_s_habitacional', 'descricao': '29038: Endividamento das famílias com o Sistema Financeiro Nacional exceto crédito habitacional em relação à renda acumulada dos últimos 12 meses (RNDBF)', 'unidade':'%', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4393/dados', 'tabela': 'confianca_consumidor', 'descricao': '4393: Índice de Confiança do Consumidor', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.7341/dados', 'tabela': 'confianca_industrial', 'descricao': '7341: Índice de Confiança do Empresário Industrial (ICEI) - Geral', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.17660/dados', 'tabela': 'confianca_servicos', 'descricao': '17660: Sondagem de Serviços - Índice de Confiança de Serviços', 'unidade':'Índice', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1402/dados', 'tabela': 'energia_comercial', 'descricao': '1402: Consumo de energia elétrica - Brasil - Comercial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1403/dados', 'tabela': 'energia_residencial', 'descricao': '1403: Consumo de energia elétrica - Brasil - Residencial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1404/dados', 'tabela': 'energia_industrial', 'descricao': '1404: Consumo de energia elétrica - Brasil - Industrial', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1405/dados', 'tabela': 'energia_outros', 'descricao': '1405: Consumo de energia elétrica - Brasil - Outros', 'unidade':'GWh', 'periodicidade': 'M'},
    {'url': 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.1406/dados', 'tabela': 'energia_total', 'descricao': '1406: Consumo de energia elétrica - Brasil - Total', 'unidade':'GWh', 'periodicidade': 'M'}
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
    sucesso = False
    tentativas = 0
    max_tentativas = 5
    
    while not sucesso and tentativas < max_tentativas:
        try:
            response = requests.get(serie['url'], params=params)
            response.raise_for_status()  # Lança a exceção
            
            data = response.json()
            df = pd.DataFrame(data)
            
            # Inserir dados no banco de dados
            df.to_sql(serie['tabela'], engine, if_exists='replace', index=False, schema='dbo')
            print(f"Dados da série {serie['tabela']} salvos com sucesso no banco de dados.")
            
            sucesso = True
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição para a série {serie['tabela']}: {e}")
            tentativas += 1
            sleep(10)
    
    if not sucesso:
        print(f"Falha ao obter dados da série {serie['tabela']} após {max_tentativas} tentativas.")
        
print("Fim das importações de dados do BACEN.")