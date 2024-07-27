import os
import streamlit as st
from st_pages import Page, show_pages

st.set_page_config(
    page_title="Dados Econômicos",
    page_icon="favicon.ico",  # Certifique-se de que o favicon.ico está no mesmo diretório
    layout="wide"
)

show_pages(
    [   Page("main.py", "Principal", "📚"),
        Page("pages/pib.py", "PIB", "📈"),
        Page("pages/populacao.py", "População", "👥"),
        Page("pages/desemprego.py", "Desemprego", "📉"),
        Page("pages/renda.py", "Renda", "💰"),
        Page("pages/inflacao.py", "Inflação", "📈"),
        Page("pages/juros.py", "Juros", "💲"),
        Page("pages/cambio.py", "Câmbio", "💱"),
        Page("pages/educacao.py", "Educação", "📚"),
        Page("pages/confianca.py", "Confiança", "📊"),
        Page("pages/energia.py", "Energia", "⚡")
    ]
)

# Título para a página principal
st.title("Sobre nós")
st.write("Bem-vindo à página inicial do projeto de Dados Econômicos.")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Wind", "9 mph", "-8%")
col5.metric("Humidity", "86%", "4%")

st.markdown("### 👨‍🔧 Data Engineering Zoomcamp by [DataTalksClub](https://datatalks.club/)")

st.image("https://pbs.twimg.com/media/FmmYA2YWYAApPRB.png")

st.info("Original Course Repository on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp)")

st.markdown("---")
