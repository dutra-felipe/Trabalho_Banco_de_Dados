import streamlit as st
from utils import column_map_veiculos
from db import run_query


def list_veiculos():
    st.subheader("Listagem de Veículos")
    
    # Filtrando por ID da unidade (filtro opcional)
    filtro_unidade = st.number_input("Filtrar por ID da Unidade", min_value=0, step=1, value=0)

    # Definindo os filtros baseados no mapeamento
    filter_conditions = []
    if filtro_unidade > 0:
        filter_conditions.append(f"v.id_unidade = {filtro_unidade}")
    
    filter_query = " AND ".join(filter_conditions) if filter_conditions else "1"

    # Exibindo as opções de ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_veiculos.keys()))
    sort_column_db = column_map_veiculos[sort_column]
    
    # Realizando a consulta
    query = f"""
        SELECT v.id_veiculo, v.id_unidade, v.placa, v.modelo, v.cor
        FROM VEICULOS v
        WHERE {filter_query}
        ORDER BY {sort_column_db}
    """
    
    veiculos = run_query(query)

    # Exibindo os veículos
    if veiculos:
        for veiculo in veiculos:
            st.write(f"ID Veículo: {veiculo['id_veiculo']} | Unidade: {veiculo['id_unidade']} | "
                     f"Placa: {veiculo['placa']} | Modelo: {veiculo['modelo']} | "
                     f"Cor: {veiculo['cor']}")
    else:
        st.warning("Nenhum veículo encontrado com os critérios fornecidos.")


def get_unidades():
    """Consulta os IDs das unidades disponíveis no banco de dados."""
    query = "SELECT id_unidade FROM UNIDADES ORDER BY id_unidade"
    unidades = run_query(query)
    return [u["id_unidade"] for u in unidades] if unidades else []


# Função para adicionar um novo veículo
def add_veiculo():
    st.subheader("Cadastrar Novo Veículo")
    
    # Consultar unidades disponíveis
    unidades_disponiveis = get_unidades()
    if not unidades_disponiveis:
        st.warning("Nenhuma unidade encontrada no banco de dados. Cadastre uma unidade primeiro.")
        return
    
    # Seleção de unidade e outros dados
    id_unidade = st.selectbox("ID da Unidade", unidades_disponiveis)
    placa = st.text_input("Placa").strip().upper()
    modelo = st.text_input("Modelo").strip()
    cor = st.text_input("Cor").strip()
    
    if st.button("Salvar Veículo"):
        # Validação básica
        if not (placa and modelo and id_unidade):
            st.error("Todos os campos obrigatórios devem ser preenchidos.")
            return
        
        query = """
            INSERT INTO VEICULOS (id_unidade, placa, modelo, cor) 
            VALUES (%s, %s, %s, %s)
        """
        try:
            run_query(query, (id_unidade, placa, modelo, cor))
            st.success("Veículo cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar veículo: {e}")