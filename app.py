import streamlit as st
import requests

st.set_page_config(page_title="E-commerce Admin", layout="centered")

URL_API = "https://comercio-eletronico-api-csharp-production.up.railway.app/api/categoria"

st.title("Painel de Controle - Categorias")
st.subheader("Integração Python (Front-end) + C# (Back-end)")
st.write("---")

# Criando abas visuais na tela
aba_listar, aba_cadastrar = st.tabs(["📋 Listar Categorias", "➕ Cadastrar Nova"])

# ================= ABAS: LISTAR CATEGORIAS =================
with aba_listar:
    st.markdown("### Categorias Cadastradas no Sistema")
    
    if st.button("🔄 Atualizar Lista"):
        try:
            # Faz a chamada GET para a API C#
            resposta = requests.get(URL_API)
            
            if resposta.status_code == 200:
                dados = resposta.json()
                
                if dados:
                    # O Streamlit cria uma tabela linda e interativa automaticamente!
                    st.dataframe(dados, use_container_width=True)
                else:
                    st.info("Nenhuma categoria encontrada no arquivo JSON.")
            else:
                st.error(f"Erro na API: Status {resposta.status_code}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Não foi possível conectar à API C#. O servidor back-end está ligado?")

# ================= ABAS: CADASTRAR CATEGORIA =================
with aba_cadastrar:
    st.markdown("### Formulário de Cadastro")
    
    # Campo de texto visual
    nova_descricao = st.text_input("Nome/Descrição da Categoria", placeholder="Ex: Informática, Roupas, Livros...")
    
    if st.button("Salvar Categoria", type="primary"):
        if nova_descricao.strip() == "":
            st.warning("Por favor, digite uma descrição válida.")
        else:
            try:
                # Monta o JSON igualzinho ao que o C# (CategoriaInputModel) espera
                payload = {"descricao": nova_descricao}
                
                # Faz a chamada POST enviando os dados
                resposta = requests.post(URL_API, json=payload)
                
                if resposta.status_code in [200, 201]:
                    st.success(f"Sucesso! Categoria '{nova_descricao}' gravada via API no JSON.")
                else:
                    st.error(f"Erro ao salvar: {resposta.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Erro de conexão. Certifique-se que o projeto C# está rodando.")