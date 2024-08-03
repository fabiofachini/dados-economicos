import streamlit as st
from st_pages import show_pages_from_config, add_page_title

# Configurações iniciais da página
st.set_page_config(
    page_title="Dados Econômicos",
    page_icon="favicon.ico",
    layout="wide"
)

# Carrega as páginas do arquivo de configuração (toml)
show_pages_from_config()

# Conteúdo da página principal
st.title("Dados da Economia Brasileira")
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
