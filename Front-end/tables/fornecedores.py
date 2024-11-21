import streamlit as st
from db import run_query
from utils import column_map_fornecedores

# Função para listar Fornecedores com filtros e ordenação
def list_fornecedores():
    st.subheader("Listagem de Fornecedores")

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_fornecedores.keys()))
    sort_column_db = column_map_fornecedores[sort_column]
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta
    query = f"SELECT * FROM FORNECEDORES ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    fornecedores = run_query(query)

    if not fornecedores:
        st.warning("Nenhum fornecedor encontrado.")
        return

    # Exibindo os resultados
    for fornecedor in fornecedores:
        st.write(f"ID: {fornecedor['id_fornecedor']} | Razão Social: {fornecedor['razao_social']} | "
                 f"CNPJ: {fornecedor['cnpj']} | Telefone: {fornecedor['telefone'] or 'N/A'} | "
                 f"Email: {fornecedor['email'] or 'N/A'}")


# Função para adicionar um novo Fornecedor
def add_fornecedor():
    st.subheader("Cadastrar Novo Fornecedor")

    razao_social = st.text_input("Razão Social").strip()
    cnpj = st.text_input("CNPJ").strip()
    telefone = st.text_input("Telefone (Opcional)").strip()
    email = st.text_input("Email (Opcional)").strip()

    if st.button("Salvar Fornecedor"):
        if not (razao_social and cnpj):
            st.error("Razão Social e CNPJ são obrigatórios.")
            return

        query = """
            INSERT INTO FORNECEDORES (razao_social, cnpj, telefone, email) 
            VALUES (%s, %s, %s, %s)
        """
        try:
            run_query(query, (razao_social, cnpj, telefone or None, email or None))
            st.success("Fornecedor cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar fornecedor: {e}")
