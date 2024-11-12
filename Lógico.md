```mermaid
erDiagram
    UNIDADES {
        PK id_unidade INT
        bloco VARCHAR(10)
        numero VARCHAR(10)
        metragem DECIMAL
        vagas_garagem INT
    }

    MORADORES {
        PK id_morador INT
        FK id_unidade INT
        nome VARCHAR(100)
        cpf VARCHAR(11)
        email VARCHAR(100)
        telefone VARCHAR(20)
        data_cadastro DATE
        ativo BOOLEAN
    }

    VEICULOS {
        PK id_veiculo INT
        FK id_unidade INT
        placa VARCHAR(8)
        modelo VARCHAR(50)
        cor VARCHAR(30)
    }

    VISITANTES {
        PK id_visitante INT
        nome VARCHAR(100)
        documento VARCHAR(20)
        telefone VARCHAR(20)
        data_cadastro DATETIME
    }

    AUTORIZACOES_VISITANTES {
        PK id_autorizacao INT
        FK id_morador INT
        FK id_visitante INT
        data_autorizacao DATETIME
        data_validade DATE
    }

    AREAS_COMUNS {
        PK id_area INT
        nome VARCHAR(50)
        capacidade INT
        taxa_uso DECIMAL
        requer_reserva BOOLEAN
    }

    RESERVAS {
        PK id_reserva INT
        FK id_morador INT
        FK id_area INT
        data_hora_inicio DATETIME
        data_hora_fim DATETIME
        valor DECIMAL
        status ENUM
    }

    TAXAS {
        PK id_taxa INT
        descricao VARCHAR(100)
        valor_base DECIMAL
        recorrente BOOLEAN
    }

    FATURAS {
        PK id_fatura INT
        FK id_unidade INT
        data_vencimento DATE
        valor_total DECIMAL
        status ENUM
    }

    ITENS_FATURA {
        PK id_item INT
        FK id_fatura INT
        FK id_taxa INT
        valor DECIMAL
    }

    FUNCIONARIOS {
        PK id_funcionario INT
        nome VARCHAR(100)
        cargo VARCHAR(50)
        data_admissao DATE
        ativo BOOLEAN
    }

    OCORRENCIAS {
        PK id_ocorrencia INT
        FK id_morador INT
        FK id_funcionario INT
        data_registro DATETIME
        descricao TEXT
        status ENUM
        prioridade ENUM
    }

    FORNECEDORES {
        PK id_fornecedor INT
        razao_social VARCHAR(100)
        cnpj VARCHAR(14)
        telefone VARCHAR(20)
        email VARCHAR(100)
    }

    SERVICOS {
        PK id_servico INT
        descricao VARCHAR(100)
        periodicidade VARCHAR(50)
    }

    CONTRATOS {
        PK id_contrato INT
        FK id_fornecedor INT
        FK id_servico INT
        data_inicio DATE
        data_fim DATE
        valor DECIMAL
        status ENUM
    }

    MORADORES ||--|| UNIDADES : "pertence"
    VEICULOS }|--|| UNIDADES : "pertence"
    MORADORES ||--|{ AUTORIZACOES_VISITANTES : "autoriza"
    VISITANTES ||--|{ AUTORIZACOES_VISITANTES : "é autorizado"
    MORADORES ||--|{ RESERVAS : "realiza"
    RESERVAS }|--|| AREAS_COMUNS : "utiliza"
    UNIDADES ||--|{ FATURAS : "possui"
    FATURAS ||--|{ ITENS_FATURA : "contém"
    ITENS_FATURA }|--|| TAXAS : "relaciona"
    MORADORES ||--|{ OCORRENCIAS : "registra"
    OCORRENCIAS }|--|| FUNCIONARIOS : "atende"
    FORNECEDORES ||--|{ CONTRATOS : "possui"
    CONTRATOS }|--|| SERVICOS : "especifica"
```