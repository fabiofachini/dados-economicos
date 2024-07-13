import pyodbc
import time
import subprocess
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def connect_to_db():
    retries = 3
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

# Chamando a função para executar os scripts
if __name__ == "__main__":
    # Estabelece a conexão com o banco de dados
    connection = connect_to_db()
    
    # Executa os scripts de ETL
    executar_scripts()

    print("Extração, carregamento e transformação dos dados do BACEN e do IBGE finalizados.")