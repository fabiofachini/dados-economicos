import requests
import pandas as pd

# Lista de URLs, descritores e descrições
series = [
    {'url': 'https://apisidra.ibge.gov.br/values/t/1846/n1/all/v/all/p/all/c11255/90707/d/v585%200', 'tabela': '1846', 'descricao': 'PIB Valores a preços correntes', 'unidade':'R$ Milhões', 'periodicidade': 'T'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/5932/n1/all/v/6564/p/all/c11255/90707/d/v6564%201', 'tabela': '5932', 'descricao': 'PIB Taxa de variação do índice de volume trimestral - Taxa trimestre contra trimestre imediatamente anterior', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6784/n1/all/v/93,9808,9810,9812,9814/p/all/d/v9810%201,v9812%202,v9814%201', 'tabela': '6784', 'descricao': 'Produto Interno Bruto, Produto Interno Bruto per capita Anual', 'unidade':'R$ Milhões'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6022/n1/all/v/606/p/all', 'tabela': '6022', 'descricao': 'População - Total - Trimestral', 'unidade':'Mil pessoas'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6415/n1/all/v/all/p/all/d/v6541%201', 'tabela': '6415', 'descricao': 'População - Total - Anual', 'unidade':'Mil pessoas'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6706/n1/all/v/606/p/all/c2/all/c58/all', 'tabela': '6706', 'descricao': 'População residente, por sexo e grupos de idade - Pirâmide etária', 'unidade':'Mil pessoas'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6318/n1/all/v/1641/p/all/c629/all', 'tabela': '6318', 'descricao': 'Pessoas de 14 anos ou mais de idade - Total - por condição em relação à força de trabalho e condição de ocupação', 'unidade':'Mil pessoas'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6380/n1/all/v/4098/p/all/d/v4098%201', 'tabela': '6380', 'descricao': 'Nível da desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade - Total', 'unidade':'Mil pessoas'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/4099/p/all/d/v4099%201', 'tabela': '6381', 'descricao': 'Taxa de desocupação, na semana de referência, das pessoas de 14 anos ou mais de idade - Total', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6785/n1/all/v/9819/p/all/d/v9819%201', 'tabela': '6785', 'descricao': 'Taxa de subocupação por insuficiência de horas trabalhadas - Total', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6807/n1/all/v/9869/p/all/d/v9869%201', 'tabela': '6807', 'descricao': 'Percentual de pessoas desalentadas na população na força de trabalho ou desalentada - Total', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/8513/n1/all/v/12466/p/all/d/v12466%201', 'tabela': '8513', 'descricao': 'Taxa de informalidade das pessoas de 14 anos ou mais de idade, ocupadas na semana de referência - Total', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/5944/n1/all/v/4096/p/all/d/v4096%201', 'tabela': '5944', 'descricao': 'Taxa de participação na força de trabalho, na semana de referência, das pessoas de 14 anos ou mais de idade - Total', 'unidade':'%'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6392/n1/all/v/6293/p/all', 'tabela': '6392', 'descricao': 'Massa de rendimento mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido em todos os trabalhos - Total', 'unidade':'Milhões de Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6393/n1/all/v/6295/p/all', 'tabela': '6393', 'descricao': 'Massa de rendimento mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, efetivamente recebido em todos os trabalhos - Total', 'unidade':'Milhões de Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6391/n1/all/v/5932/p/all/c888/all', 'tabela': '6391', 'descricao': 'Rendimento médio mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido no trabalho principal - Total - por grupamento de atividade no trabalho principal', 'unidade':'Milhões de Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6389/n1/all/v/5932/p/all/c11913/all', 'tabela': '6389', 'descricao': 'Rendimento médio mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, habitualmente recebido no trabalho principal - Total - por posição na ocupação e categoria do emprego no trabalho principal', 'unidade':'Milhões de Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6388/n1/all/v/5934/p/all', 'tabela': '6388', 'descricao': 'Rendimento médio mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, efetivamente recebido no trabalho principal - Total', 'unidade':'Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/6387/n1/all/v/5935/p/all', 'tabela': '6387', 'descricao': 'Rendimento médio mensal real das pessoas de 14 anos ou mais de idade ocupadas na semana de referência com rendimento de trabalho, efetivamente recebido em todos os trabalhos - Total', 'unidade':'Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7453/n1/all/v/10806/p/all/d/v10806%203', 'tabela': '7453', 'descricao': 'Índice de Gini do rendimento médio mensal real das pessoas de 14 anos ou mais - Índice'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7438/n1/all/v/10769/p/all/c1019/all', 'tabela': '7438', 'descricao': 'Limites superiores das classes de percentual das pessoas em ordem crescente de rendimento domiciliar per capita, a preços médios do ano - Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7521/n1/all/v/606,8412/p/all/c1019/all/d/v8412%201', 'tabela': '7521', 'descricao': 'População residente, por classes simples de percentual das pessoas por rendimento domiciliar per capita, a preços médios do ano'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7527/n1/all/v/10826/p/all/c1019/all/d/v10826%201', 'tabela': '7527', 'descricao': 'Distribuição da massa de rendimento mensal real domiciliar per capita, a preços médios do ano, por classes simples de percentual das pessoas em ordem crescente de rendimento domiciliar per capita - %'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7531/n1/all/v/10824/p/all/c1019/all', 'tabela': '7531', 'descricao': 'Rendimento médio mensal real domiciliar per capita, a preços médios do ano, por classes simples de percentual das pessoas em ordem crescente de rendimento domiciliar per capita - Reais'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7113/n1/all/v/10267/p/all/c2/all/c58/2795/d/v10267%201', 'tabela': '7113', 'descricao': 'Taxa de analfabetismo das pessoas de 15 anos ou mais de idade'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/7267/n1/all/v/1641/p/all/c2/all/c1568/all', 'tabela': '7267', 'descricao': 'Pessoas de 14 anos ou mais de idade por sexo e nível de instrução'},
    {'url': 'https://apisidra.ibge.gov.br/values/t/2296/n1/all/v/48/p/all/d/v48%202', 'tabela': '2296', 'descricao': 'Custo médio m² em moeda corrente - Reais'},
]

# Parâmetros da requisição
parametros = {'formato': 'json'}

# Dicionário para armazenar DataFrames
dataframes = {}

# Loop para iterar sobre as séries
for serie in series:
    url = serie['url']
    tabela = serie['tabela']
    descricao = serie['descricao']
    
    # Faz a requisição
    resposta = requests.get(url, params=parametros)
    
    # Conferir se não apresenta erro
    if resposta.status_code == 200:
        # Salva a resposta json
        data = resposta.json()

        # Transforma os dados em um DataFrame
        df = pd.DataFrame(data)

        # Define a primeira linha como nomes das colunas
        colunas = df.iloc[0]
        df.columns = colunas

        # Remove a primeira linha, que agora são os nomes das colunas
        df = df[1:]

        # Reseta o índice do DataFrame
        df = df.reset_index(drop=True)

        # Armazena o DataFrame no dicionário
        dataframes[tabela] = df

        # Imprime o DataFrame e a descrição para verificação
        print(f'Tabela {tabela} - {descricao}')
        print(dataframes[tabela])
        
    else:
        print(f'Erro na tabela {tabela}:', resposta.status_code)