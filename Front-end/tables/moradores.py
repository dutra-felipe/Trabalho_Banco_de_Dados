import streamlit as st
from db import run_query
from utils import column_map_moradores


# Função para listar Moradores com filtros e ordenação
def list_moradores():
    st.subheader("Listagem de Moradores")

    # Carregar Unidades disponíveis para o filtro
    unidades_query = "SELECT id_unidade, bloco, numero FROM UNIDADES"
    unidades = run_query(unidades_query)

    if not unidades:
        st.warning("Nenhuma unidade cadastrada. Não será possível filtrar por unidade.")
        unidade_options = {"Todos": None}
    else:
        unidade_options = {"Todos": None}
        unidade_options.update({f"{u['bloco']} - {u['numero']} (ID: {u['id_unidade']})": u['id_unidade'] for u in unidades})

    unidade_selecionada = st.selectbox("Filtrar por Unidade", list(unidade_options.keys()))

    # Obter o ID da unidade selecionada
    id_unidade_filtro = unidade_options[unidade_selecionada]

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_moradores.keys()))
    sort_column_db = column_map_moradores[sort_column]  # Nome da coluna no banco de dados
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com filtros e JOIN
    query = """
        SELECT m.*, u.bloco, u.numero
        FROM MORADORES m
        JOIN UNIDADES u ON m.id_unidade = u.id_unidade
        WHERE 1=1
    """
    params = []

    if id_unidade_filtro is not None:
        query += " AND m.id_unidade = %s"
        params.append(id_unidade_filtro)

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    moradores = run_query(query, params)

    if not moradores:
        st.warning("Nenhum morador encontrado.")
        return

    # Exibindo os resultados com informações da unidade
    for morador in moradores:
        st.write(f"ID: {morador['id_morador']} | Nome: {morador['nome']} | "
                 f"CPF: {morador['cpf']} | Email: {morador['email'] or 'N/A'} | "
                 f"Telefone: {morador['telefone'] or 'N/A'} | "
                 f"Unidade: {morador['bloco']} - {morador['numero']} (ID: {morador['id_unidade']}) | "
                 f"Ativo: {'Sim' if morador['ativo'] else 'Não'} | "
                 f"Data de Cadastro: {morador['data_cadastro']}")


# Função para adicionar um novo Morador
def add_morador():
    st.subheader("Cadastrar Novo Morador")

    # Carregar Unidades disponíveis
    unidades_query = "SELECT id_unidade, bloco, numero FROM UNIDADES"
    unidades = run_query(unidades_query)

    if not unidades:
        st.error("Nenhuma unidade cadastrada. Cadastre unidades antes de adicionar moradores.")
        return

    # Criar lista de opções para o Selectbox
    unidade_options = {f"{u['bloco']} - {u['numero']} (ID: {u['id_unidade']})": u['id_unidade'] for u in unidades}
    unidade_selecionada = st.selectbox("Unidade", list(unidade_options.keys()))

    # Entradas do usuário
    id_unidade = unidade_options[unidade_selecionada]
    nome = st.text_input("Nome").strip()
    cpf = st.text_input("CPF (somente números)").strip()
    email = st.text_input("Email (Opcional)").strip()
    telefone = st.text_input("Telefone (Opcional)").strip()
    ativo = st.checkbox("Ativo", value=True)

    # Botão para salvar
    if st.button("Salvar Morador"):
        # Validação básica
        if not (id_unidade and nome and cpf):
            st.error("Unidade, Nome e CPF são obrigatórios.")
            return

        query = """
            INSERT INTO MORADORES (id_unidade, nome, cpf, email, telefone, ativo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            run_query(query, (id_unidade, nome, cpf, email or None, telefone or None, ativo))
            st.success("Morador cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar morador: {e}")
