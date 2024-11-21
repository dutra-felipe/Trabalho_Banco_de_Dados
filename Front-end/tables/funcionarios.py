import streamlit as st
from db import run_query
from utils import column_map_funcionarios


# Função para listar funcionários com filtros e ordenação
def list_funcionarios():
    st.subheader("Listagem de Funcionários")

    # Filtro por status (Ativo/Inativo)
    filtro_ativo = st.selectbox("Filtrar por Status", ["Todos", "Ativo", "Inativo"])

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_funcionarios.keys()))
    sort_column_db = column_map_funcionarios[sort_column]  # Convertendo para o nome da coluna no banco de dados

    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com filtros
    query = "SELECT * FROM FUNCIONARIOS WHERE 1=1"
    params = []

    if filtro_ativo != "Todos":
        query += " AND ativo = %s"
        params.append(True if filtro_ativo == "Ativo" else False)

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    funcionarios = run_query(query, params)

    if not funcionarios:
        st.warning("Nenhum funcionário encontrado.")
        return

    # Exibindo os resultados
    for funcionario in funcionarios:
        st.write(f"ID: {funcionario['id_funcionario']} | Nome: {funcionario['nome']} | "
                 f"Cargo: {funcionario['cargo']} | Data de Admissão: {funcionario['data_admissao']} | "
                 f"Ativo: {'Sim' if funcionario['ativo'] else 'Não'}")


# Função para adicionar um novo funcionário
def add_funcionario():
    st.subheader("Cadastrar Novo Funcionário")

    # Entradas do usuário
    nome = st.text_input("Nome").strip()
    cargo = st.text_input("Cargo").strip()
    data_admissao = st.date_input("Data de Admissão")
    ativo = st.checkbox("Ativo", value=True)

    # Botão para salvar
    if st.button("Salvar Funcionário"):
        # Validação básica
        if not (nome and cargo and data_admissao):
            st.error("Todos os campos obrigatórios devem ser preenchidos.")
            return

        query = """
            INSERT INTO FUNCIONARIOS (nome, cargo, data_admissao, ativo) 
            VALUES (%s, %s, %s, %s)
        """
        try:
            run_query(query, (nome, cargo, data_admissao, ativo))
            st.success("Funcionário cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar funcionário: {e}")
