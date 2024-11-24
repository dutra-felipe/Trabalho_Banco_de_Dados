import streamlit as st
from db import run_query
from utils import column_map_unidades


def add_unidade():
    st.subheader("Cadastrar Nova Unidade")
    bloco = st.text_input("Bloco")
    numero = st.text_input("Número")
    metragem = st.number_input("Metragem", min_value=0.0, format="%.2f")
    vagas_garagem = st.number_input("Vagas de Garagem", min_value=1, step=1)

    if st.button("Salvar Unidade"):
        query = """
            INSERT INTO UNIDADES (bloco, numero, metragem, vagas_garagem)
            VALUES (%s, %s, %s, %s)
        """
        run_query(query, (bloco, numero, metragem, vagas_garagem))
        st.success("Unidade cadastrada com sucesso!")


def list_unidades():
    st.subheader("Listagem de Unidades")

    # Filtro de ordenação
    sort_column_display = st.selectbox("Ordenar por", list(column_map_unidades.keys()))
    sort_order = st.radio("Ordem", ["Crescente", "Decrescente"])

    # Obter o nome da coluna no banco de dados usando o mapeamento
    sort_column = column_map_unidades.get(sort_column_display)

    # Determinar a direção de ordenação
    order_by = "ASC" if sort_order == "Crescente" else "DESC"

    # Ajustar a consulta SQL com base na escolha do usuário
    query = f"SELECT * FROM UNIDADES ORDER BY {sort_column} {order_by}"

    unidades = run_query(query)
    if unidades is None or len(unidades) == 0:
        st.warning("Nenhuma unidade encontrada ou erro ao buscar dados.")
        return

    for unidade in unidades:
        st.write(f"Bloco: {unidade['bloco']} | Número: {unidade['numero']} | Metragem: {unidade['metragem']} | Vagas: {unidade['vagas_garagem']}")
