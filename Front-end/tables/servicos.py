import streamlit as st
from db import run_query
from utils import column_map_servicos

# Função para listar Serviços com filtros e ordenação
def list_servicos():
    st.subheader("Listagem de Serviços")

    sort_column = st.selectbox("Ordenar por", list(column_map_servicos.keys()))
    sort_column_db = column_map_servicos[sort_column]
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    query = f"SELECT * FROM SERVICOS ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    servicos = run_query(query)

    if not servicos:
        st.warning("Nenhum serviço encontrado.")
        return

    for servico in servicos:
        st.write(f"ID: {servico['id_servico']} | Descrição: {servico['descricao']} | "
                 f"Periodicidade: {servico['periodicidade'] or 'N/A'}")


# Função para adicionar um novo Serviço
def add_servico():
    st.subheader("Cadastrar Novo Serviço")

    descricao = st.text_input("Descrição").strip()
    periodicidade = st.text_input("Periodicidade").strip()

    if st.button("Salvar Serviço"):
        if not descricao:
            st.error("A descrição é obrigatória.")
            return

        query = """
            INSERT INTO SERVICOS (descricao, periodicidade) 
            VALUES (%s, %s)
        """
        try:
            run_query(query, (descricao, periodicidade or None))
            st.success("Serviço cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar serviço: {e}")
