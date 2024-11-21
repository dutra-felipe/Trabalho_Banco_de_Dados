import streamlit as st
from db import run_query
from utils import column_map_contratos


# Função para listar Contratos com filtros e ordenação
def list_contratos():
    st.subheader("Listagem de Contratos")

    # Carregar Fornecedores e Serviços disponíveis para o filtro
    fornecedores_query = "SELECT id_fornecedor, razao_social FROM FORNECEDORES"
    fornecedores = run_query(fornecedores_query)

    servicos_query = "SELECT id_servico, descricao FROM SERVICOS"
    servicos = run_query(servicos_query)

    # Configuração dos filtros de Fornecedor e Serviço
    fornecedor_options = {"Todos": None}
    if fornecedores:
        fornecedor_options.update({f"{f['id_fornecedor']} - {f['razao_social']}": f['id_fornecedor'] for f in fornecedores})

    servico_options = {"Todos": None}
    if servicos:
        servico_options.update({f"{s['id_servico']} - {s['descricao']}": s['id_servico'] for s in servicos})

    fornecedor_selecionado = st.selectbox("Filtrar por Fornecedor", list(fornecedor_options.keys()))
    servico_selecionado = st.selectbox("Filtrar por Serviço", list(servico_options.keys()))

    # Obter IDs selecionados
    id_fornecedor_filtro = fornecedor_options[fornecedor_selecionado]
    id_servico_filtro = servico_options[servico_selecionado]

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_contratos.keys()))
    sort_column_db = column_map_contratos[sort_column]  # Nome da coluna no banco de dados
    sort_order = st.selectbox("Ordem", ["Ascendente", "Descendente"])

    # Montar a consulta com filtros
    query = "SELECT * FROM CONTRATOS WHERE 1=1"
    params = []

    if id_fornecedor_filtro:
        query += " AND id_fornecedor = %s"
        params.append(id_fornecedor_filtro)
    if id_servico_filtro:
        query += " AND id_servico = %s"
        params.append(id_servico_filtro)

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    contratos = run_query(query, params)

    if not contratos:
        st.warning("Nenhum contrato encontrado.")
        return

    # Exibindo os resultados
    for contrato in contratos:
        st.write(f"ID: {contrato['id_contrato']} | Fornecedor: {contrato['id_fornecedor']} | "
                 f"Serviço: {contrato['id_servico']} | Data Início: {contrato['data_inicio']} | "
                 f"Data Fim: {contrato['data_fim'] or 'Indefinida'} | "
                 f"Valor: R${contrato['valor']:.2f} | Status: {contrato['status']}")

# Função para adicionar um novo Contrato
def add_contrato():
    st.subheader("Cadastrar Novo Contrato")

    # Carregar Fornecedores e Serviços disponíveis
    fornecedores_query = "SELECT id_fornecedor, razao_social FROM FORNECEDORES"
    fornecedores = run_query(fornecedores_query)

    servicos_query = "SELECT id_servico, descricao FROM SERVICOS"
    servicos = run_query(servicos_query)

    if not fornecedores or not servicos:
        st.error("Cadastre fornecedores e serviços antes de adicionar contratos.")
        return

    # Seleção de Fornecedor e Serviço
    fornecedor_options = {f"{f['id_fornecedor']} - {f['razao_social']}": f['id_fornecedor'] for f in fornecedores}
    servico_options = {f"{s['id_servico']} - {s['descricao']}": s['id_servico'] for s in servicos}

    fornecedor_selecionado = st.selectbox("Fornecedor", list(fornecedor_options.keys()))
    servico_selecionado = st.selectbox("Serviço", list(servico_options.keys()))

    # Entradas do usuário
    data_inicio = st.date_input("Data de Início")
    data_fim = st.date_input("Data de Fim (Opcional)", value=None)
    valor = st.number_input("Valor", min_value=0.0, format="%.2f")
    status = st.selectbox("Status", ['Ativo', 'Encerrado', 'Cancelado'])

    # Botão para salvar
    if st.button("Salvar Contrato"):
        if not (data_inicio and valor):
            st.error("Data de início e valor são obrigatórios.")
            return

        query = """
            INSERT INTO CONTRATOS (id_fornecedor, id_servico, data_inicio, data_fim, valor, status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            run_query(query, (
                fornecedor_options[fornecedor_selecionado], 
                servico_options[servico_selecionado],
                data_inicio, data_fim, valor, status
            ))
            st.success("Contrato cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar contrato: {e}")
