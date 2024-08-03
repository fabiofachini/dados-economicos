import os
import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="Dados Econômicos",
    page_icon="favicon.ico",  # Certifique-se de que o favicon.ico está no mesmo diretório
    layout="wide"
)

show_pages(
    [   Page("main.py", "Principal", "🏠"),
        Page("pages/pib.py", "PIB", "📊"),
        Page("pages/populacao.py", "População", "👥"),
        Page("pages/desemprego.py", "Desemprego", "📉"),
        Page("pages/desigualdade.py", "Desigualdade", "⚖️"),
        Page("pages/renda.py", "Renda", "💰"),
        Page("pages/inflacao.py", "Inflação", "💸"),
        Page("pages/juros.py", "Juros", "📈"),
        Page("pages/credito.py", "Crédito", "💳"),
        Page("pages/cambio.py", "Câmbio", "💱"),
        Page("pages/educacao.py", "Educação", "📚"),
        Page("pages/confianca.py", "Confiança", "👍"),
        Page("pages/energia.py", "Energia", "⚡")
    ]
)

# Título para a página principal
st.title("Dados da Economia Brasileira")
# Descrição Inicial
st.write("""
Bem-vindo ao projeto de engenharia e análise de Dados Econômicos da Economia Brasileira.
Este projeto tem como objetivo fornecer informações atualizadas sobre a economia do Brasil
através de dados coletados de fontes confiáveis, como IBGE e BACEN.
Os dados são processados e disponibilizados diariamente às 09h.
""")
st.info("Acesse o código no repositório [Github](https://github.com/fabiofachini/dados-economicos)")

st.markdown("### 🏛️ Diagrama da Arquitetura")

st.image("img.gif")

st.markdown("---")

# Créditos dos Desenvolvedores
st.markdown("### 👥 Desenvolvido por:")
st.write("""
- 👨‍💻 [Fábio Fachini](https://www.linkedin.com/in/fabio-fachini/)
- 👨‍💼 [Felipe Sens Bonetto](https://www.linkedin.com/in/felipe-sens-bonetto-128235144/)
- 👨‍🔧 [Julio Bonckewitz](https://www.linkedin.com/in/bonckewitz/)
""")