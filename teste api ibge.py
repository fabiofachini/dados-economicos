import requests
import pandas as pd

# Define the URL and parameters for the SIDRA API
url = "https://apisidra.ibge.gov.br/values/t/6022/n1/all/v/606/p/all"

# Make the API request
response = requests.get(url)
data = response.json()

# Convert the JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Usar a primeira linha como nomes de colunas
new_columns = df.iloc[0]
df.columns = new_columns

# Remover a primeira linha, que agora são os nomes das colunas
df = df[1:]

# Reiniciar o índice do DataFrame
df = df.reset_index(drop=True)

# Display the DataFrame
print(df)
