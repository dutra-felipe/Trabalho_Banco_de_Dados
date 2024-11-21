import streamlit as st
from db import run_query
from utils import column_map_areas_comuns

# Função para listar Áreas Comuns com filtros e ordenação
def list_areas_comuns():
    st.subheader("Listagem de Áreas Comuns")

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_areas_comuns.keys()))
    sort_column_db = column_map_areas_comuns[sort_column]  # Nome da coluna no banco de dados
    sort_order = st.radio("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta
    query = f"SELECT * FROM AREAS_COMUNS ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"
    areas_comuns = run_query(query)

    if not areas_comuns:
        st.warning("Nenhuma área comum encontrada.")
        return

    # Exibindo os resultados
    for area in areas_comuns:
        st.write(
            f"ID: {area['id_area']} | Nome: {area['nome']} | "
            f"Capacidade: {area['capacidade']} | Taxa de Uso: {area['taxa_uso'] or 'N/A'} | "
            f"Necessidade de Reserva: {'Sim' if area['requer_reserva'] else 'Não'}"
        )

# Função para adicionar uma nova área comum
def add_area_comum():
    st.subheader("Cadastrar Nova Área Comum")

    # Entradas do usuário
    nome = st.text_input("Nome").strip()
    capacidade = st.number_input("Capacidade", min_value=0, step=1, format="%d")
    taxa_uso = st.number_input("Taxa de Uso (Opcional)", min_value=0.0, step=0.01, format="%.2f")
    requer_reserva = st.checkbox("Requer Reserva", value=False)

    # Botão para salvar
    if st.button("Salvar Área Comum"):
        # Validação básica
        if not nome:
            st.error("O campo Nome é obrigatório.")
            return

        query = """
            INSERT INTO AREAS_COMUNS (nome, capacidade, taxa_uso, requer_reserva) 
            VALUES (%s, %s, %s, %s)
        """
        try:
            run_query(query, (nome, capacidade, taxa_uso or None, requer_reserva))
            st.success("Área comum cadastrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar área comum: {e}")
