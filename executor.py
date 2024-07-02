import subprocess
import os

# Função para executar scripts Python
def executar_scripts():
    try:
        # Caminho para os arquivos api_ibge.py e api_bacen.py na pasta source
        source_path = os.path.join(os.getcwd(), 'source')

        # Executa api_ibge.py
        print("Executando api_ibge.py...")
        ibge_script = os.path.join(source_path, 'api_ibge.py')
        subprocess.run(['python3', ibge_script])

        # Executa api_bacen.py
        print("Executando api_bacen.py...")
        bacen_script = os.path.join(source_path, 'api_bacen.py')
        subprocess.run(['python3', bacen_script])

        # Executa dbt run
        print("Executando dbt run...")
        subprocess.run(['dbt', 'run'])

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script: {e}")

# Chamando a função para executar os scripts
if __name__ == "__main__":
    executar_scripts()