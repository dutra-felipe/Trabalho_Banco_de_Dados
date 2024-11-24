import streamlit as st
from db import run_query


# Função para adicionar um novo item de fatura
def add_item_fatura():
    st.subheader("Adicionar Item à Fatura")

    # Buscar faturas existentes
    faturas = run_query("SELECT id_fatura FROM FATURAS")
    if not faturas:
        st.warning("Nenhuma fatura encontrada. Cadastre uma fatura primeiro.")
        return

    # Buscar taxas existentes
    taxas = run_query("SELECT id_taxa, descricao FROM TAXAS")
    if not taxas:
        st.warning("Nenhuma taxa encontrada. Cadastre uma taxa primeiro.")
        return

    # Inputs para adicionar o item
    fatura_selecionada = st.selectbox("ID da Fatura", sorted([f["id_fatura"] for f in faturas]))
    taxa_selecionada = st.selectbox("ID da Taxa", [f"{t['id_taxa']} - {t['descricao']}" for t in taxas])
    valor = st.number_input("Valor", min_value=0.01, format="%.2f")

    if st.button("Adicionar Item"):
        id_taxa = int(taxa_selecionada.split(" - ")[0])  # Pega o ID da taxa selecionada
        query = """
            INSERT INTO ITENS_FATURA (id_fatura, id_taxa, valor)
            VALUES (%s, %s, %s)
        """
        run_query(query, (fatura_selecionada, id_taxa, valor))
        st.success("Item adicionado à fatura com sucesso!")


# Função para listar os itens de fatura com filtros
def list_itens_fatura():
    st.subheader("Listagem de Itens de Fatura")

    # Filtros
    filtro_fatura = st.selectbox("Filtrar por ID da Fatura", ["Todos"] + [f["id_fatura"] for f in run_query("SELECT id_fatura FROM FATURAS")])
    filtro_taxa = st.selectbox("Filtrar por ID da Taxa", ["Todos"] + [t["id_taxa"] for t in run_query("SELECT id_taxa FROM TAXAS")])
    sort_column = st.selectbox("Ordenar por", ["ID Item", "ID Fatura", "ID Taxa", "Valor"])
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com os filtros
    query = "SELECT * FROM ITENS_FATURA WHERE 1=1"
    params = []

    if filtro_fatura != "Todos":
        query += " AND id_fatura = %s"
        params.append(filtro_fatura)

    if filtro_taxa != "Todos":
        query += " AND id_taxa = %s"
        params.append(filtro_taxa)

    if sort_order == "Ascendente":
        query += f" ORDER BY {sort_column.replace(' ', '_').lower()} ASC"
    else:
        query += f" ORDER BY {sort_column.replace(' ', '_').lower()} DESC"

    itens_fatura = run_query(query, params)

    if not itens_fatura:
        st.warning("Nenhum item encontrado.")
        return

    for item in itens_fatura:
        st.write(f"ID Item: {item['id_item']} | ID Fatura: {item['id_fatura']} | ID Taxa: {item['id_taxa']} | Valor: R$ {item['valor']:.2f}")
