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
        SELECT v.id_veiculo, v.id_unidade, u.bloco, u.numero, v.placa, v.modelo, v.cor
        FROM VEICULOS v
        JOIN UNIDADES u ON v.id_unidade = u.id_unidade
        WHERE {filter_query}
        ORDER BY v.{sort_column_db}
    """

    veiculos = run_query(query)

    # Exibindo os veículos
    if veiculos:
        for veiculo in veiculos:
            st.write(f"ID Veículo: {veiculo['id_veiculo']} | Unidade: Bloco {veiculo['bloco']}, Número {veiculo['numero']} | "
                     f"Placa: {veiculo['placa']} | Modelo: {veiculo['modelo']} | "
                     f"Cor: {veiculo['cor']}")
    else:
        st.warning("Nenhum veículo encontrado com os critérios fornecidos.")


def get_unidades():
    """Consulta os IDs das unidades disponíveis no banco de dados."""
    query = "SELECT id_unidade, bloco, numero FROM UNIDADES ORDER BY id_unidade"
    unidades = run_query(query)
    return {f"{u['bloco']}-{u['numero']}": u['id_unidade'] for u in unidades} if unidades else {}


# Função para adicionar um novo veículo
def add_veiculo():
    st.subheader("Cadastrar Novo Veículo")

    # Consultar unidades disponíveis
    unidades_disponiveis = get_unidades()
    if not unidades_disponiveis:
        st.warning("Nenhuma unidade encontrada no banco de dados. Cadastre uma unidade primeiro.")
        return

    # Seleção de unidade e outros dados
    unidade_selecionada = st.selectbox("Unidade", list(unidades_disponiveis.keys()))
    id_unidade = unidades_disponiveis[unidade_selecionada]  # Obtemos o id_unidade real
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
            run_query(query, (id_unidade, placa, modelo, cor))  # Agora 'id_unidade' é numérico
            st.success("Veículo cadastrado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar veículo: {e}")
