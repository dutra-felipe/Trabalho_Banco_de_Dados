import streamlit as st
from tables.unidades import list_unidades, add_unidade
from tables.faturas import list_faturas, add_fatura
from tables.taxas import list_taxas, add_taxa
from tables.veiculos import list_veiculos, add_veiculo
from tables.itens_fatura import list_itens_fatura, add_item_fatura
from tables.funcionarios import list_funcionarios, add_funcionario
from tables.ocorrencias import list_ocorrencias, add_ocorrencia
from tables.visitantes import list_visitantes, add_visitante
from tables.moradores import list_moradores, add_morador
from tables.areas_comuns import list_areas_comuns, add_area_comum
from tables.reservas import list_reservas, add_reserva
from tables.autoriza_visitante import list_autorizacoes, add_autorizacao
from tables.fornecedores import list_fornecedores, add_fornecedor
from tables.servicos import list_servicos, add_servico
from tables.contratos import list_contratos, add_contrato


def show_menu():
    st.title("Sistema de Gestão de Condomínios")
    menu = st.sidebar.selectbox("Menu", ["Áreas Comuns", "Autorização de Visitantes", "Contratos de Serviços", "Faturas", "Fornecedores", "Funcionários", "Itens da Fatura", "Moradores","Ocorrências", "Reservas de Áreas Comuns", "Serviços", "Taxas", "Unidades", "Veículos", "Visitantes"])
    return menu


# Função para lidar com as ações da tabela "Áreas Comuns"
def handle_areas_comuns():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_area_comum()
    elif op == "Listar":
        list_areas_comuns()

# Função para lidar com as ações da tabela "Autorização de Visitantes"
def handle_autorizacoes():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_autorizacao()
    elif op == "Listar":
        list_autorizacoes()

# Função para lidar com as ações da tabela "Contratos"
def handle_contratos():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_contrato()
    elif op == "Listar":
        list_contratos()

# Função para lidar com as ações da tabela "Faturas"
def handle_faturas():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_fatura()
    elif op == "Listar":
        list_faturas()

# Função para lidar com as ações da tabela "Fornecedores"
def handle_fornecedores():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_fornecedor()
    elif op == "Listar":
        list_fornecedores()

# Função para lidar com as ações da tabela "Funcionários"
def handle_funcionarios():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_funcionario()
    elif op == "Listar":
        list_funcionarios()

# Função para lidar com as ações da tabela "Fatura"
def handle_itens_fatura():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_item_fatura()
    elif op == "Listar":
        list_itens_fatura()

# Função para lidar com as ações da tabela "Moradores"
def handle_moradores():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_morador()
    elif op == "Listar":
        list_moradores()

# Função para lidar com as ações da tabela "Ocorrências"
def handle_ocorrencias():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_ocorrencia()
    elif op == "Listar":
        list_ocorrencias()

# Função para lidar com as ações da tabela "Reservas"
def handle_reservas():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_reserva()
    elif op == "Listar":
        list_reservas()

# Função para lidar com as ações da tabela "Serviços"
def handle_servicos():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_servico()
    elif op == "Listar":
        list_servicos()

# Função para lidar com as ações da tabela "Moradores"
def handle_taxas():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_taxa()
    elif op == "Listar":
        list_taxas()

def handle_unidades():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_unidade()
    elif op == "Listar":
        list_unidades()

# Função para lidar com as ações da tabela "Visitantes"
def handle_veiculos():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_veiculo()
    elif op == "Listar":
        list_veiculos()

# Função para lidar com as ações da tabela "Visitantes"
def handle_visitantes():
    op = st.radio("Ações", ["Adicionar", "Listar"])
    if op == "Adicionar":
        add_visitante()
    elif op == "Listar":
        list_visitantes()
