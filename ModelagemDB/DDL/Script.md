```SQL

-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS gestao_condominio;
USE gestao_condominio;

-- Tabela UNIDADES
CREATE TABLE UNIDADES (
    id_unidade INT PRIMARY KEY AUTO_INCREMENT,
    bloco VARCHAR(10) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    metragem DECIMAL(6,2) NOT NULL,
    vagas_garagem INT NOT NULL DEFAULT 1,
    CONSTRAINT uk_bloco_numero UNIQUE (bloco, numero)
);

-- Tabela MORADORES
CREATE TABLE MORADORES (
    id_morador INT PRIMARY KEY AUTO_INCREMENT,
    id_unidade INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_cadastro DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_morador_unidade FOREIGN KEY (id_unidade) 
        REFERENCES UNIDADES(id_unidade)
);

-- Tabela VEICULOS
CREATE TABLE VEICULOS (
    id_veiculo INT PRIMARY KEY AUTO_INCREMENT,
    id_unidade INT NOT NULL,
    placa VARCHAR(8) NOT NULL UNIQUE,
    modelo VARCHAR(50) NOT NULL,
    cor VARCHAR(30),
    CONSTRAINT fk_veiculo_unidade FOREIGN KEY (id_unidade) 
        REFERENCES UNIDADES(id_unidade)
);

-- Tabela VISITANTES
CREATE TABLE VISITANTES (
    id_visitante INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    documento VARCHAR(20) NOT NULL,
    telefone VARCHAR(20),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabela AUTORIZACOES_VISITANTES
CREATE TABLE AUTORIZACOES_VISITANTES (
    id_autorizacao INT PRIMARY KEY AUTO_INCREMENT,
    id_morador INT NOT NULL,
    id_visitante INT NOT NULL,
    data_autorizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_validade DATE,
    CONSTRAINT fk_autorizacao_morador FOREIGN KEY (id_morador) 
        REFERENCES MORADORES(id_morador),
    CONSTRAINT fk_autorizacao_visitante FOREIGN KEY (id_visitante) 
        REFERENCES VISITANTES(id_visitante)
);

-- Tabela AREAS_COMUNS
CREATE TABLE AREAS_COMUNS (
    id_area INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    capacidade INT,
    taxa_uso DECIMAL(10,2),
    requer_reserva BOOLEAN DEFAULT FALSE
);

-- Tabela RESERVAS
CREATE TABLE RESERVAS (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    id_morador INT NOT NULL,
    id_area INT NOT NULL,
    data_hora_inicio DATETIME NOT NULL,
    data_hora_fim DATETIME NOT NULL,
    valor DECIMAL(10,2),
    status ENUM('Pendente', 'Confirmada', 'Cancelada') DEFAULT 'Pendente',
    CONSTRAINT fk_reserva_morador FOREIGN KEY (id_morador) 
        REFERENCES MORADORES(id_morador),
    CONSTRAINT fk_reserva_area FOREIGN KEY (id_area) 
        REFERENCES AREAS_COMUNS(id_area)
);

-- Tabela TAXAS
CREATE TABLE TAXAS (
    id_taxa INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100) NOT NULL,
    valor_base DECIMAL(10,2) NOT NULL,
    recorrente BOOLEAN DEFAULT TRUE
);

-- Tabela FATURAS
CREATE TABLE FATURAS (
    id_fatura INT PRIMARY KEY AUTO_INCREMENT,
    id_unidade INT NOT NULL,
    data_vencimento DATE NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    status ENUM('Pendente', 'Paga', 'Atrasada') DEFAULT 'Pendente',
    CONSTRAINT fk_fatura_unidade FOREIGN KEY (id_unidade) 
        REFERENCES UNIDADES(id_unidade)
);

-- Tabela ITENS_FATURA
CREATE TABLE ITENS_FATURA (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_fatura INT NOT NULL,
    id_taxa INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_item_fatura FOREIGN KEY (id_fatura) 
        REFERENCES FATURAS(id_fatura),
    CONSTRAINT fk_item_taxa FOREIGN KEY (id_taxa) 
        REFERENCES TAXAS(id_taxa)
);

-- Tabela FUNCIONARIOS
CREATE TABLE FUNCIONARIOS (
    id_funcionario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    data_admissao DATE NOT NULL,
    ativo BOOLEAN DEFAULT TRUE
);

-- Tabela OCORRENCIAS
CREATE TABLE OCORRENCIAS (
    id_ocorrencia INT PRIMARY KEY AUTO_INCREMENT,
    id_morador INT NOT NULL,
    id_funcionario INT,
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT NOT NULL,
    status ENUM('Aberta', 'Em Andamento', 'Resolvida', 'Cancelada') DEFAULT 'Aberta',
    prioridade ENUM('Baixa', 'Média', 'Alta') DEFAULT 'Média',
    CONSTRAINT fk_ocorrencia_morador FOREIGN KEY (id_morador) 
        REFERENCES MORADORES(id_morador),
    CONSTRAINT fk_ocorrencia_funcionario FOREIGN KEY (id_funcionario) 
        REFERENCES FUNCIONARIOS(id_funcionario)
);

-- Tabela FORNECEDORES
CREATE TABLE FORNECEDORES (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    razao_social VARCHAR(100) NOT NULL,
    cnpj VARCHAR(14) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela SERVICOS
CREATE TABLE SERVICOS (
    id_servico INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(100) NOT NULL,
    periodicidade VARCHAR(50)
);

-- Tabela CONTRATOS
CREATE TABLE CONTRATOS (
    id_contrato INT PRIMARY KEY AUTO_INCREMENT,
    id_fornecedor INT NOT NULL,
    id_servico INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE,
    valor DECIMAL(10,2) NOT NULL,
    status ENUM('Ativo', 'Encerrado', 'Cancelado') DEFAULT 'Ativo',
    CONSTRAINT fk_contrato_fornecedor FOREIGN KEY (id_fornecedor) 
        REFERENCES FORNECEDORES(id_fornecedor),
    CONSTRAINT fk_contrato_servico FOREIGN KEY (id_servico) 
        REFERENCES SERVICOS(id_servico)
);

-- Criação de índices adicionais para otimização
CREATE INDEX idx_morador_unidade ON MORADORES(id_unidade);
CREATE INDEX idx_veiculo_unidade ON VEICULOS(id_unidade);
CREATE INDEX idx_fatura_unidade ON FATURAS(id_unidade);
CREATE INDEX idx_reserva_data ON RESERVAS(data_hora_inicio);
CREATE INDEX idx_ocorrencia_status ON OCORRENCIAS(status);
CREATE INDEX idx_contrato_status ON CONTRATOS(status);

```