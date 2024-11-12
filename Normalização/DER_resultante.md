```mermaid

erDiagram
    UNIDADES ||--|{ MORADORES : possui
    UNIDADES ||--|{ VEICULOS : possui
    UNIDADES ||--|{ FATURAS : gera
    MORADORES ||--|{ AUTORIZACOES_VISITANTES : autoriza
    VISITANTES ||--|{ AUTORIZACOES_VISITANTES : "é autorizado"
    MORADORES ||--|{ RESERVAS : realiza
    AREAS_COMUNS ||--|{ RESERVAS : "é reservada"
    FATURAS ||--|{ ITENS_FATURA : contém
    TAXAS ||--|{ ITENS_FATURA : compõe
    MORADORES ||--|{ OCORRENCIAS : registra
    FUNCIONARIOS ||--|{ OCORRENCIAS : atende
    FORNECEDORES ||--|{ CONTRATOS : possui
    SERVICOS ||--|{ CONTRATOS : especifica

    UNIDADES {
        PK id_unidade
        bloco
        numero
        metragem
        vagas_garagem
    }

    MORADORES {
        PK id_morador
        FK id_unidade
        nome
        cpf
        email
        telefone
        data_cadastro
        ativo
    }

    VEICULOS {
        PK id_veiculo
        FK id_unidade
        placa
        modelo
        cor
    }

    VISITANTES {
        PK id_visitante
        nome
        documento
        telefone
    }

    AUTORIZACOES_VISITANTES {
        PK id_autorizacao
        FK id_morador
        FK id_visitante
        data_autorizacao
        data_validade
    }

    AREAS_COMUNS {
        PK id_area
        nome
        capacidade
        taxa_uso
        requer_reserva
    }

    RESERVAS {
        PK id_reserva
        FK id_morador
        FK id_area
        data_hora_inicio
        data_hora_fim
        valor
        status
    }

    TAXAS {
        PK id_taxa
        descricao
        valor_base
        recorrente
    }

    FATURAS {
        PK id_fatura
        FK id_unidade
        data_vencimento
        valor_total
        status
    }

    ITENS_FATURA {
        PK id_item
        FK id_fatura
        FK id_taxa
        valor
    }

    FUNCIONARIOS {
        PK id_funcionario
        nome
        cargo
        data_admissao
        ativo
    }

    OCORRENCIAS {
        PK id_ocorrencia
        FK id_morador
        FK id_funcionario
        data_registro
        descricao
        status
        prioridade
    }

    FORNECEDORES {
        PK id_fornecedor
        razao_social
        cnpj
        telefone
        email
    }

    SERVICOS {
        PK id_servico
        descricao
        periodicidade
    }

    CONTRATOS {
        PK id_contrato
        FK id_fornecedor
        FK id_servico
        data_inicio
        data_fim
        valor
        status
    }
```