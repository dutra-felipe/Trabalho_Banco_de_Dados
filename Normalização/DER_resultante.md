erDiagram
    MORADOR ||--|| UNIDADE : "mora em"
    UNIDADE ||--|{ VEICULO : "possui"
    MORADOR ||--|{ AUTORIZACAO_VISITANTE : "cria"
    VISITANTE ||--|{ AUTORIZACAO_VISITANTE : "recebe"
    MORADOR ||--|{ RESERVA : "realiza"
    RESERVA ||--|| AREA_COMUM : "utiliza"
    UNIDADE ||--|{ FATURA : "possui"
    FATURA ||--|{ ITENS_FATURA : "contém"
    TAXA ||--|{ ITENS_FATURA : "compõe"
    MORADOR ||--|{ OCORRENCIA : "registra"
    OCORRENCIA ||--|| FUNCIONARIO : "atende"
    FORNECEDOR ||--|{ CONTRATO : "possui"
    CONTRATO ||--|| SERVICO : "especifica"

    MORADOR {
        int id_morador PK
        int id_unidade FK
        string nome
        string cpf
        string telefone
        string email
        date data_cadastro
        boolean ativo
    }

    UNIDADE {
        int id_unidade PK
        string bloco
        string numero
        int metragem
        int vagas_garagem
    }

    VISITANTE {
        int id_visitante PK
        string nome
        string documento
        string telefone
        datetime data_cadastro
    }

    AUTORIZACAO_VISITANTE {
        int id_autorizacao PK
        int id_morador FK
        int id_visitante FK
        datetime data_autorizacao
        datetime data_validade
    }

    AREA_COMUM {
        int id_area PK
        string nome
        int capacidade
        decimal taxa_uso
        boolean requer_reserva
    }

    RESERVA {
        int id_reserva PK
        int id_morador FK
        int id_area FK
        datetime data_hora_inicio
        datetime data_hora_fim
        decimal valor
        string status
    }

    FATURA {
        int id_fatura PK
        int id_unidade FK
        date data_vencimento
        decimal valor_total
        string status
    }

    ITENS_FATURA {
        int id_item PK
        int id_fatura FK
        int id_taxa FK
        decimal valor
    }

    TAXA {
        int id_taxa PK
        string descricao
        decimal valor_base
        boolean recorrente
    }

    OCORRENCIA {
        int id_ocorrencia PK
        int id_morador FK
        int id_funcionario FK
        datetime data_registro
        string descricao
        string status
        string prioridade
    }

    FUNCIONARIO {
        int id_funcionario PK
        string nome
        string cargo
        date data_admissao
        boolean ativo
    }

    FORNECEDOR {
        int id_fornecedor PK
        string razao_social
        string cnpj
        string telefone
        string email
    }

    CONTRATO {
        int id_contrato PK
        int id_fornecedor FK
        int id_servico FK
        date data_inicio
        date data_fim
        decimal valor
        string status
    }

    SERVICO {
        int id_servico PK
        string descricao
        string periodicidade
    }

    VEICULO {
        int id_veiculo PK
        int id_unidade FK
        string placa
        string modelo
        string cor
    }
```