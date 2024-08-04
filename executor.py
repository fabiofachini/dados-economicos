import pyodbc
import time
import subprocess
import os
import requests
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

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

# Função para executar scripts Python
def executar_scripts():
    try:
        # Caminho para os arquivos api_ibge.py e api_bacen.py na pasta source
        source_path = os.path.join(os.getcwd(), 'source')

        # Executa api_ibge.py
        print("Executando api_ibge.py")
        ibge_script = os.path.join(source_path, 'api_ibge.py')
        subprocess.run(['python3', ibge_script])

        # Executa api_bacen.py
        print("Executando api_bacen.py")
        bacen_script = os.path.join(source_path, 'api_bacen.py')
        subprocess.run(['python3', bacen_script])

        # Define a variável de ambiente para o profiles.yml
        os.environ['DBT_PROFILES_DIR'] = os.getenv('DBT_PROFILES_DIR', '.')

        # Executa dbt run
        print("Executando dbt run")
        subprocess.run(['dbt', 'run'])

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")

def acessar_paginas_streamlit():
    urls = [
        "http://20.14.251.70:8501/PIB",
        "http://20.14.251.70:8501/População",
        "http://20.14.251.70:8501/Desemprego",
        "http://20.14.251.70:8501/Desigualdade",
        "http://20.14.251.70:8501/Renda",
        "http://20.14.251.70:8501/Inflação",
        "http://20.14.251.70:8501/Juros",
        "http://20.14.251.70:8501/Crédito",
        "http://20.14.251.70:8501/Câmbio",
        "http://20.14.251.70:8501/Educação",
        "http://20.14.251.70:8501/Confiança",
        "http://20.14.251.70:8501/Energia"
    ]
    
    for url in urls:
        try:
            response = requests.get(url)
            time.sleep(5)
            if response.status_code == 200:
                print(f"Página acessada com sucesso: {url}")
            else:
                print(f"Falha ao acessar a página {url}: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a página {url}: {e}")

# Chamando a função para executar os scripts
if __name__ == "__main__":
    # Estabelece a conexão com o banco de dados
    connection = connect_to_db()
    
    # Executa os scripts de ETL
    executar_scripts()

    # Acessa as páginas do Streamlit para carregar o cache
    acessar_paginas_streamlit()

    print("Extração, carregamento e transformação dos dados do BACEN e do IBGE finalizados.")