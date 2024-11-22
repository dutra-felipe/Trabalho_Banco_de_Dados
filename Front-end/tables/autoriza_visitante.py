import streamlit as st
from db import run_query
from utils import column_map_autorizacoes


# Função para listar Autorizações de Visitantes com filtros e ordenação
def list_autorizacoes():
    st.subheader("Listagem de Autorizações de Visitantes")

    # Carregar Moradores e Visitantes para filtro opcional
    moradores_query = "SELECT id_morador, nome FROM MORADORES WHERE ativo = TRUE"
    moradores = run_query(moradores_query)

    visitantes_query = "SELECT id_visitante, nome FROM VISITANTES"
    visitantes = run_query(visitantes_query)

    # Filtro de Morador
    morador_options = {"Todos": None}
    if moradores:
        morador_options.update({f"{m['id_morador']} - {m['nome']}": m['id_morador'] for m in moradores})
    morador_selecionado = st.selectbox("Filtrar por Morador", list(morador_options.keys()))

    # Filtro de Visitante
    visitante_options = {"Todos": None}
    if visitantes:
        visitante_options.update({f"{v['id_visitante']} - {v['nome']}": v['id_visitante'] for v in visitantes})
    visitante_selecionado = st.selectbox("Filtrar por Visitante", list(visitante_options.keys()))

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_autorizacoes.keys()))
    sort_column_db = column_map_autorizacoes[sort_column]
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com JOINs e filtros
    query = """
        SELECT a.id_autorizacao, a.data_autorizacao, a.data_validade,
               m.nome AS nome_morador, v.nome AS nome_visitante
        FROM AUTORIZACOES_VISITANTES a
        JOIN MORADORES m ON a.id_morador = m.id_morador
        JOIN VISITANTES v ON a.id_visitante = v.id_visitante
        WHERE 1=1
    """
    params = []

    if morador_options[morador_selecionado]:
        query += " AND a.id_morador = %s"
        params.append(morador_options[morador_selecionado])

    if visitante_options[visitante_selecionado]:
        query += " AND a.id_visitante = %s"
        params.append(visitante_options[visitante_selecionado])

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    autorizacoes = run_query(query, params)

    if not autorizacoes:
        st.warning("Nenhuma autorização encontrada.")
        return

    # Exibindo os resultados com nomes
    for autorizacao in autorizacoes:
        st.write(
            f"ID: {autorizacao['id_autorizacao']} | Morador: {autorizacao['nome_morador']} | "
            f"Visitante: {autorizacao['nome_visitante']} | Data de Autorização: {autorizacao['data_autorizacao']} | "
            f"Validade: {autorizacao['data_validade'] or 'Indeterminada'}"
        )


# Função para adicionar uma nova autorização de visitante
def add_autorizacao():
    st.subheader("Cadastrar Nova Autorização de Visitante")

    # Carregar Moradores
    moradores_query = "SELECT id_morador, nome FROM MORADORES WHERE ativo = TRUE"
    moradores = run_query(moradores_query)

    if not moradores:
        st.error("Nenhum morador ativo encontrado. Cadastre moradores antes de criar autorizações.")
        return

    morador_options = {f"{m['id_morador']} - {m['nome']}": m['id_morador'] for m in moradores}
    morador_selecionado = st.selectbox("Selecione o Morador", list(morador_options.keys()))

    # Carregar Visitantes
    visitantes_query = "SELECT id_visitante, nome FROM VISITANTES"
    visitantes = run_query(visitantes_query)

    if not visitantes:
        st.error("Nenhum visitante encontrado. Cadastre visitantes antes de criar autorizações.")
        return

    visitante_options = {f"{v['id_visitante']} - {v['nome']}": v['id_visitante'] for v in visitantes}
    visitante_selecionado = st.selectbox("Selecione o Visitante", list(visitante_options.keys()))

    # Entrada da data de validade da autorização
    data_validade = st.date_input("Data de Validade (Opcional)", value=None)

    # Botão para salvar
    if st.button("Salvar Autorização"):
        # Validação básica
        if not (morador_selecionado and visitante_selecionado):
            st.error("Morador e Visitante são obrigatórios.")
            return

        query = """
            INSERT INTO AUTORIZACOES_VISITANTES (id_morador, id_visitante, data_validade) 
            VALUES (%s, %s, %s)
        """
        try:
            run_query(
                query,
                (
                    morador_options[morador_selecionado],
                    visitante_options[visitante_selecionado],
                    data_validade or None
                )
            )
            st.success("Autorização cadastrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar autorização: {e}")
