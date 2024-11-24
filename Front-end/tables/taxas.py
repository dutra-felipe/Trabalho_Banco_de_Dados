import streamlit as st
from db import run_query
from utils import column_map_taxas


# Função para listar taxas com filtros
def list_taxas():
    st.subheader("Listagem de Taxas")

    # Filtro de Recorrência
    filtro_recorrente = st.selectbox("Filtrar por Recorrência", ["Todos", "Sim", "Não"])

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_taxas.keys()))  # Usando as chaves do mapeamento
    sort_column_db = column_map_taxas[sort_column]  # Convertendo para o nome da coluna no banco de dados

    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com filtros
    query = "SELECT * FROM TAXAS WHERE 1=1"
    params = []

    if filtro_recorrente != "Todos":
        query += " AND recorrente = %s"
        params.append(True if filtro_recorrente == "Sim" else False)

    if sort_order == "Ascendente":
        query += f" ORDER BY {sort_column_db} ASC"
    else:
        query += f" ORDER BY {sort_column_db} DESC"

    taxas = run_query(query, params)

    if not taxas:
        st.warning("Nenhuma taxa encontrada.")
        return

    # Exibindo os resultados
    for taxa in taxas:
        st.write(f"Descrição: {taxa['descricao']} | Valor Base: {taxa['valor_base']} | Recorrente: {'Sim' if taxa['recorrente'] else 'Não'}")


# Função para adicionar uma nova taxa
def add_taxa():
    st.subheader("Cadastrar Nova Taxa")
    descricao = st.text_input("Descrição")
    valor_base = st.number_input("Valor Base", min_value=0.0, format="%.2f")
    recorrente = st.selectbox("Recorrente", ["Sim", "Não"])

    if st.button("Salvar Taxa"):
        query = """
            INSERT INTO TAXAS (descricao, valor_base, recorrente)
            VALUES (%s, %s, %s)
        """
        run_query(query, (descricao, valor_base, True if recorrente == "Sim" else False))
        st.success("Taxa cadastrada com sucesso!")
