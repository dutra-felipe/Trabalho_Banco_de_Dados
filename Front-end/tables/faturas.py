import streamlit as st
from db import run_query
from utils import column_map_faturas


def get_unidades():
    """Consulta os IDs das unidades disponíveis no banco de dados."""
    query = "SELECT id_unidade, bloco, numero FROM UNIDADES ORDER BY id_unidade"
    unidades = run_query(query)
    return {f"{u['bloco']}-{u['numero']}": u['id_unidade'] for u in unidades} if unidades else {}


def list_faturas():
    st.subheader("Listagem de Faturas")
    
    # Filtrando com base no ID da unidade (filtro opcional)
    filtro_unidade = st.number_input("Filtrar por ID da Unidade", min_value=0, step=1, value=0)

    # Definindo os filtros baseados no mapeamento de colunas
    filter_conditions = []
    if filtro_unidade > 0:
        filter_conditions.append(f"f.id_unidade = {filtro_unidade}")
    
    # Convertendo o filtro para uma consulta SQL
    filter_query = " AND ".join(filter_conditions) if filter_conditions else "1"

    # Exibindo as opções de ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_faturas.keys()))
    sort_column_db = column_map_faturas[sort_column]  # Convertendo para o nome da coluna no banco de dados
    
    # Realizando a consulta com a ordenação e filtro aplicados
    query = f"""
        SELECT f.id_fatura, f.id_unidade, u.bloco, u.numero, f.data_vencimento, f.valor_total, f.status
        FROM FATURAS f
        JOIN UNIDADES u ON f.id_unidade = u.id_unidade
        WHERE {filter_query}
        ORDER BY f.{sort_column_db}
    """
    
    faturas = run_query(query)

    # Exibindo as faturas
    if faturas:
        for fatura in faturas:
            st.write(f"ID Fatura: {fatura['id_fatura']} | Unidade: Bloco {fatura['bloco']}, Número {fatura['numero']} | "
                     f"Data Vencimento: {fatura['data_vencimento']} | "
                     f"Valor Total: R${fatura['valor_total']:.2f} | Status: {fatura['status']}")
    else:
        st.warning("Nenhuma fatura encontrada com os critérios fornecidos.")


def add_fatura():
    st.subheader("Cadastrar Nova Fatura")
    
    # Consultar unidades disponíveis
    unidades_disponiveis = get_unidades()
    if not unidades_disponiveis:
        st.warning("Nenhuma unidade encontrada no banco de dados. Cadastre uma unidade primeiro.")
        return

    # Seleção dos dados da fatura
    unidade_selecionada = st.selectbox("Unidade", list(unidades_disponiveis.keys()))
    id_unidade = unidades_disponiveis[unidade_selecionada]  # Obtemos o id_unidade real
    data_vencimento = st.date_input("Data de Vencimento")
    valor_total = st.number_input("Valor Total", min_value=0.0, format="%.2f")
    status = st.selectbox("Status", ["Pendente", "Paga", "Atrasada"])
    
    if st.button("Salvar Fatura"):
        # Validação básica
        if not (id_unidade and data_vencimento and valor_total > 0):
            st.error("Todos os campos obrigatórios devem ser preenchidos corretamente.")
            return
        
        query = """
            INSERT INTO FATURAS (id_unidade, data_vencimento, valor_total, status) 
            VALUES (%s, %s, %s, %s)
        """
        try:
            run_query(query, (id_unidade, data_vencimento, valor_total, status))
            st.success("Fatura cadastrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar fatura: {e}")
