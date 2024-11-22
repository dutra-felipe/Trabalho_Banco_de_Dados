import streamlit as st
from db import run_query
from utils import column_map_reservas


# Função para listar Reservas com filtros e ordenação
def list_reservas():
    st.subheader("Listagem de Reservas")

    # Filtros por status
    status_filter = st.selectbox("Filtrar por Status", ["Todos", "Pendente", "Confirmada", "Cancelada"])

    # Ordenação
    sort_column = st.selectbox("Ordenar por", list(column_map_reservas.keys()))
    sort_column_db = column_map_reservas[sort_column]  # Nome da coluna no banco de dados
    sort_order = st.radio("Ordem", ["Ascendente", "Descendente"])

    # Montando a consulta com filtros e JOINs
    query = """
        SELECT r.id_reserva, r.data_hora_inicio, r.data_hora_fim, r.valor, r.status,
               m.nome AS nome_morador, a.nome AS nome_area
        FROM RESERVAS r
        JOIN MORADORES m ON r.id_morador = m.id_morador
        JOIN AREAS_COMUNS a ON r.id_area = a.id_area
        WHERE 1=1
    """
    params = []

    if status_filter != "Todos":
        query += " AND r.status = %s"
        params.append(status_filter)

    query += f" ORDER BY {sort_column_db} {'ASC' if sort_order == 'Ascendente' else 'DESC'}"

    reservas = run_query(query, params)

    if not reservas:
        st.warning("Nenhuma reserva encontrada.")
        return

    # Exibindo os resultados com nomes detalhados
    for reserva in reservas:
        st.write(
            f"ID: {reserva['id_reserva']} | Morador: {reserva['nome_morador']} | "
            f"Área: {reserva['nome_area']} | Início: {reserva['data_hora_inicio']} | "
            f"Fim: {reserva['data_hora_fim']} | Valor: {reserva['valor'] or 'N/A'} | "
            f"Status: {reserva['status']}"
        )


# Função para adicionar uma nova Reserva
def add_reserva():
    st.subheader("Cadastrar Nova Reserva")

    # Carregar Moradores disponíveis
    moradores_query = "SELECT id_morador, nome FROM MORADORES WHERE ativo = TRUE"
    moradores = run_query(moradores_query)

    if not moradores:
        st.error("Nenhum morador ativo encontrado. Cadastre moradores antes de registrar reservas.")
        return

    morador_options = {f"{m['id_morador']} - {m['nome']}": m['id_morador'] for m in moradores}
    morador_selecionado = st.selectbox("Selecione o Morador", list(morador_options.keys()))

    # Carregar Áreas Comuns disponíveis
    areas_query = "SELECT id_area, nome FROM AREAS_COMUNS"
    areas = run_query(areas_query)

    if not areas:
        st.error("Nenhuma área comum cadastrada. Cadastre áreas antes de registrar reservas.")
        return

    area_options = {f"{a['id_area']} - {a['nome']}": a['id_area'] for a in areas}
    area_selecionada = st.selectbox("Selecione a Área Comum", list(area_options.keys()))

    # Entradas do usuário
    data_inicio = st.date_input("Data de Início")
    hora_inicio = st.time_input("Hora de Início")
    data_fim = st.date_input("Data de Fim")
    hora_fim = st.time_input("Hora de Fim")
    valor = st.number_input("Valor da Reserva (Opcional)", min_value=0.0, step=0.01, format="%.2f")
    status = st.selectbox("Status", ["Pendente", "Confirmada", "Cancelada"])

    # Combinar data e hora
    try:
        data_hora_inicio = f"{data_inicio} {hora_inicio}"
        data_hora_fim = f"{data_fim} {hora_fim}"
    except Exception as e:
        st.error(f"Erro ao processar data e hora: {e}")
        return

    # Botão para salvar
    if st.button("Salvar Reserva"):
        # Validação básica
        if not (data_inicio and data_fim and hora_inicio and hora_fim and morador_selecionado and area_selecionada):
            st.error("Todos os campos obrigatórios devem ser preenchidos.")
            return

        if data_hora_fim <= data_hora_inicio:
            st.error("A data e hora de fim devem ser posteriores à data e hora de início.")
            return

        query = """
            INSERT INTO RESERVAS (id_morador, id_area, data_hora_inicio, data_hora_fim, valor, status) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            run_query(
                query,
                (
                    morador_options[morador_selecionado],
                    area_options[area_selecionada],
                    data_hora_inicio,
                    data_hora_fim,
                    valor or None,
                    status,
                ),
            )
            st.success("Reserva cadastrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao cadastrar reserva: {e}")
