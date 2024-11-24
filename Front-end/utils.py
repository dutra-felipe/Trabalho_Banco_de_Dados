# Mapeamento de colunas para as tabelas
column_map_areas_comuns = {
    "Nome": "nome",
    "Capacidade": "capacidade",
    "Taxa de Uso": "taxa_uso",
    "Necessidade de Reserva": "necessidade_reserva"
}

column_map_autorizacoes = {
    "ID Autorização": "a.id_autorizacao",
    "Morador": "m.nome",
    "Visitante": "v.nome",
    "Data de Autorização": "a.data_autorizacao",
    "Data de Validade": "a.data_validade"
}

column_map_contratos = {
    "ID do Fornecedor": "id_fornecedor",
    "ID do Serviço": "id_servico",
    "Data de Início": "data_inicio",
    "Data de Término": "data_fim",
    "Valor": "valor",
    "Status": "status"
}

column_map_faturas = {
    "ID da Fatura": "id_fatura",
    "ID da Unidade": "id_unidade",
    "Data de Vencimento": "data_vencimento",
    "Valor Total": "valor_total",
    "Status": "status"
}

column_map_fornecedores = {
    "Razão Social": "razao_social",
    "CNPJ": "cnpj",
    "Telefone": "telefone",
    "Email": "email"
}

column_map_itens_fatura = {
    "ID da Fatura": "id_fatura",
    "ID da Taxa": "id_taxa",
    "Valor": "valor"
}

column_map_reservas = {
    "ID Reserva": "r.id_reserva",
    "Morador": "m.nome",
    "Área": "a.nome",
    "Data Início": "r.data_hora_inicio",
    "Data Fim": "r.data_hora_fim",
    "Valor": "r.valor",
    "Status": "r.status"
}

column_map_servicos = {
    "Descrição": "descricao",
    "Periodicidade": "periodicidade"
}

column_map_taxas = {
    "Descrição": "descricao",
    "Valor Base": "valor_base",
    "Recorrente": "recorrente"
}

column_map_unidades = {
    "Bloco": "bloco",
    "Número": "numero",
    "Metragem": "metragem",
    "Vagas de Garagem": "vagas_garagem"
}

column_map_veiculos = {
    "ID da Unidade": "id_unidade",
    "Placa": "placa",
    "Modelo": "modelo",
    "Cor": "cor"
}

column_map_funcionarios = {
    "Nome": "nome",
    "Cargo": "cargo",
    "Data de Admissão": "data_admissao",
    "Ativo": "ativo"
}

column_map_ocorrencias = {
    "ID do Morador": "id_morador",
    "ID do Funcionário": "id_funcionario",
    "Data de Registro": "data_registro",
    "Descrição": "descricao",
    "Status": "status",
    "Prioridade": "prioridade"
}

column_map_visitantes = {
    "Nome": "nome",
    "Documento": "documento",
    "Telefone": "telefone",
    "Data": "data_cadastro"
}

column_map_moradores = {
    "ID da Unidade": "id_unidade",
    "Nome": "nome",
    "CPF": "cpf",
    "Email": "email",
    "Telefone": "telefone",
    "Data de Cadastro": "data_cadastro",
    "Ativo": "ativo"
}
