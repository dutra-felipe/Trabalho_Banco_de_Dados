import streamlit as st
from db import run_query
from utils import column_map_ocorrencias


# Função para carregar moradores
def get_moradores():
    query = "SELECT id_morador, nome FROM MORADORES ORDER BY nome"
    moradores = run_query(query)
    return [{"id": m["id_morador"], "nome": m["nome"]} for m in moradores]


# Função para carregar funcionários
def get_funcionarios():
    query = "SELECT id_funcionario, nome FROM FUNCIONARIOS ORDER BY nome"
    funcionarios = run_query(query)
    return [{"id": f["id_funcionario"], "nome": f["nome"]} for f in funcionarios]


# Função para listar ocorrências
def list_ocorrencias():
    st.subheader("Listagem de Ocorrências")

    # Filtros
    filtro_status = st.selectbox("Filtrar por Status", ["Todos", "Aberta", "Em Andamento", "Resolvida", "Cancelada"])
    filtro_prioridade = st.selectbox("Filtrar por Prioridade", ["Todas", "Baixa", "Média", "Alta"])

    sort_column = st.selectbox("Ordenar por", list(column_map_ocorrencias.keys()))
    sort_column_db = column_map_ocorrencias[sort_column]

    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a query
    query = "SELECT o.*, m.nome AS morador_nome, f.nome AS funcionario_nome FROM OCORRENCIAS o"
    query += " LEFT JOIN MORADORES m ON o.id_morador = m.id_morador"
    query += " LEFT JOIN FUNCIONARIOS f ON o.id_funcionario = f.id_funcionario"
    query += " WHERE 1=1"
    params = []

    if filtro_status != "Todos":
        query += " AND o.status = %s"
        params.append(filtro_status)

    if filtro_prioridade != "Todas":
        query += " AND o.prioridade = %s"
        params.append(filtro_prioridade)

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    ocorrencias = run_query(query, params)

    if not ocorrencias:
        st.warning("Nenhuma ocorrência encontrada com os critérios fornecidos.")
        return

    # Exibindo resultados
    for ocorrencia in ocorrencias:
        st.write(f"**ID:** {ocorrencia['id_ocorrencia']} | "
                 f"**Morador:** {ocorrencia['morador_nome']} | "
                 f"**Funcionário:** {ocorrencia['funcionario_nome'] or 'N/A'} | "
                 f"**Status:** {ocorrencia['status']} | **Prioridade:** {ocorrencia['prioridade']} | "
                 f"**Descrição:** {ocorrencia['descricao'][:50]}...")


# Função para adicionar uma nova ocorrência
def add_ocorrencia():
    st.subheader("Cadastrar Nova Ocorrência")

    # Carregando dados de moradores e funcionários
    moradores = get_moradores()
    funcionarios = get_funcionarios()

    if not moradores:
        st.warning("Nenhum morador encontrado. Cadastre moradores antes de registrar ocorrências.")
        return

    # Inputs do formulário
    id_morador = st.selectbox("Morador", moradores, format_func=lambda x: x["nome"])
    id_funcionario = st.selectbox("Funcionário (Opcional)", [{"id": None, "nome": "Nenhum"}] + funcionarios, 
                                  format_func=lambda x: x["nome"])
    descricao = st.text_area("Descrição", max_chars=500)
    prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
    status = st.selectbox("Status", ["Aberta", "Em Andamento", "Resolvida", "Cancelada"])

    # Salvando ocorrência
    if st.button("Salvar Ocorrência"):
        if not descricao:
            st.error("A descrição da ocorrência é obrigatória.")
            return

        query = """
            INSERT INTO OCORRENCIAS (id_morador, id_funcionario, descricao, prioridade, status)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (
            id_morador["id"],
            id_funcionario["id"] if id_funcionario["id"] else None,
            descricao,
            prioridade,
            status
        )
        try:
            run_query(query, params)
            st.success("Ocorrência cadastrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar ocorrência: {e}")
