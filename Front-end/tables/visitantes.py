import streamlit as st
from db import run_query
from utils import column_map_visitantes


# Função para listar Visitantes com filtros e ordenação
def list_visitantes():
    st.subheader("Listagem de Visitantes")

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_visitantes.keys()))
    sort_column_db = column_map_visitantes[sort_column]  # Nome da coluna no banco de dados

    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta
    query = f"SELECT * FROM VISITANTES ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    visitantes = run_query(query)

    if not visitantes:
        st.warning("Nenhum visitante encontrado.")
        return

    # Exibindo os resultados
    for visitante in visitantes:
        st.write(f"ID: {visitante['id_visitante']} | Nome: {visitante['nome']} | "
                 f"Documento: {visitante['documento']} | Telefone: {visitante['telefone'] or 'N/A'} | "
                 f"Data de Cadastro: {visitante['data_cadastro']}")


# Função para adicionar um novo visitante
def add_visitante():
    st.subheader("Cadastrar Novo Visitante")

    # Entradas do usuário
    nome = st.text_input("Nome").strip()
    documento = st.text_input("Documento (CPF ou RG)").strip()
    telefone = st.text_input("Telefone (Opcional)").strip()

    # Botão para salvar
    if st.button("Salvar Visitante"):
        # Validação básica
        if not (nome and documento):
            st.error("Nome e Documento são obrigatórios.")
            return

        query = """
            INSERT INTO VISITANTES (nome, documento, telefone)
            VALUES (%s, %s, %s)
        """
        try:
            run_query(query, (nome, documento, telefone or None))
            st.success("Visitante cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar visitante: {e}")
