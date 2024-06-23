import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

# Configurações de conexão
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
driver = os.getenv('DB_DRIVER')

try:
    # Estabelece a conexão
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()

    # Inserir dados na tabela
    cursor.execute("INSERT INTO Exemplo (id, nome, idade) VALUES (?, ?, ?)", (7, 'João', 30))
    cursor.execute("INSERT INTO Exemplo (id, nome, idade) VALUES (?, ?, ?)", (8, 'Maria', 28))
    cursor.execute("INSERT INTO Exemplo (id, nome, idade) VALUES (?, ?, ?)", (9, 'Pedro', 35))
    
    conn.commit()  # Confirma a transação

    print("Dados inseridos com sucesso.")

    # Exemplo de consulta para verificar os dados na tabela
    cursor.execute("SELECT * FROM Exemplo;")
    rows = cursor.fetchall()
    print("Dados na tabela Exemplo:")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)
