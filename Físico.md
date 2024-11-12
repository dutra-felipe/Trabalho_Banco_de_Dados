# Modelo Físico - Sistema de Gestão de Condomínios

## 1. UNIDADES
- **id_unidade**: INT [PK, AUTO_INCREMENT]
- **bloco**: VARCHAR(10) [NOT NULL]
- **numero**: VARCHAR(10) [NOT NULL]
- **metragem**: DECIMAL(6,2) [NOT NULL]
- **vagas_garagem**: INT [NOT NULL, DEFAULT 1]
- CONSTRAINT uk_bloco_numero UNIQUE (bloco, numero)

## 2. MORADORES
- **id_morador**: INT [PK, AUTO_INCREMENT]
- **id_unidade**: INT [FK, NOT NULL]
- **nome**: VARCHAR(100) [NOT NULL]
- **cpf**: VARCHAR(11) [NOT NULL, UNIQUE]
- **email**: VARCHAR(100)
- **telefone**: VARCHAR(20)
- **data_cadastro**: DATE [NOT NULL, DEFAULT CURRENT_DATE]
- **ativo**: BOOLEAN [DEFAULT TRUE]
- CONSTRAINT fk_morador_unidade FOREIGN KEY (id_unidade) REFERENCES UNIDADES(id_unidade)

## 3. VEICULOS
- **id_veiculo**: INT [PK, AUTO_INCREMENT]
- **id_unidade**: INT [FK, NOT NULL]
- **placa**: VARCHAR(8) [NOT NULL, UNIQUE]
- **modelo**: VARCHAR(50) [NOT NULL]
- **cor**: VARCHAR(30)
- CONSTRAINT fk_veiculo_unidade FOREIGN KEY (id_unidade) REFERENCES UNIDADES(id_unidade)

## 4. VISITANTES
- **id_visitante**: INT [PK, AUTO_INCREMENT]
- **nome**: VARCHAR(100) [NOT NULL]
- **documento**: VARCHAR(20) [NOT NULL]
- **telefone**: VARCHAR(20)
- **data_cadastro**: DATETIME [DEFAULT CURRENT_TIMESTAMP]

## 5. AUTORIZACOES_VISITANTES
- **id_autorizacao**: INT [PK, AUTO_INCREMENT]
- **id_morador**: INT [FK, NOT NULL]
- **id_visitante**: INT [FK, NOT NULL]
- **data_autorizacao**: DATETIME [DEFAULT CURRENT_TIMESTAMP]
- **data_validade**: DATE
- CONSTRAINT fk_autorizacao_morador FOREIGN KEY (id_morador) REFERENCES MORADORES(id_morador)
- CONSTRAINT fk_autorizacao_visitante FOREIGN KEY (id_visitante) REFERENCES VISITANTES(id_visitante)

## 6. AREAS_COMUNS
- **id_area**: INT [PK, AUTO_INCREMENT]
- **nome**: VARCHAR(50) [NOT NULL]
- **capacidade**: INT
- **taxa_uso**: DECIMAL(10,2)
- **requer_reserva**: BOOLEAN [DEFAULT FALSE]

## 7. RESERVAS
- **id_reserva**: INT [PK, AUTO_INCREMENT]
- **id_morador**: INT [FK, NOT NULL]
- **id_area**: INT [FK, NOT NULL]
- **data_hora_inicio**: DATETIME [NOT NULL]
- **data_hora_fim**: DATETIME [NOT NULL]
- **valor**: DECIMAL(10,2)
- **status**: ENUM('Pendente', 'Confirmada', 'Cancelada') [DEFAULT 'Pendente']
- CONSTRAINT fk_reserva_morador FOREIGN KEY (id_morador) REFERENCES MORADORES(id_morador)
- CONSTRAINT fk_reserva_area FOREIGN KEY (id_area) REFERENCES AREAS_COMUNS(id_area)

## 8. TAXAS
- **id_taxa**: INT [PK, AUTO_INCREMENT]
- **descricao**: VARCHAR(100) [NOT NULL]
- **valor_base**: DECIMAL(10,2) [NOT NULL]
- **recorrente**: BOOLEAN [DEFAULT TRUE]

## 9. FATURAS
- **id_fatura**: INT [PK, AUTO_INCREMENT]
- **id_unidade**: INT [FK, NOT NULL]
- **data_vencimento**: DATE [NOT NULL]
- **valor_total**: DECIMAL(10,2) [NOT NULL]
- **status**: ENUM('Pendente', 'Paga', 'Atrasada') [DEFAULT 'Pendente']
- CONSTRAINT fk_fatura_unidade FOREIGN KEY (id_unidade) REFERENCES UNIDADES(id_unidade)

## 10. ITENS_FATURA
- **id_item**: INT [PK, AUTO_INCREMENT]
- **id_fatura**: INT [FK, NOT NULL]
- **id_taxa**: INT [FK, NOT NULL]
- **valor**: DECIMAL(10,2) [NOT NULL]
- CONSTRAINT fk_item_fatura FOREIGN KEY (id_fatura) REFERENCES FATURAS(id_fatura)
- CONSTRAINT fk_item_taxa FOREIGN KEY (id_taxa) REFERENCES TAXAS(id_taxa)

## 11. FUNCIONARIOS
- **id_funcionario**: INT [PK, AUTO_INCREMENT]
- **nome**: VARCHAR(100) [NOT NULL]
- **cargo**: VARCHAR(50) [NOT NULL]
- **data_admissao**: DATE [NOT NULL]
- **ativo**: BOOLEAN [DEFAULT TRUE]

## 12. OCORRENCIAS
- **id_ocorrencia**: INT [PK, AUTO_INCREMENT]
- **id_morador**: INT [FK, NOT NULL]
- **id_funcionario**: INT [FK]
- **data_registro**: DATETIME [DEFAULT CURRENT_TIMESTAMP]
- **descricao**: TEXT [NOT NULL]
- **status**: ENUM('Aberta', 'Em Andamento', 'Resolvida', 'Cancelada') [DEFAULT 'Aberta']
- **prioridade**: ENUM('Baixa', 'Média', 'Alta') [DEFAULT 'Média']
- CONSTRAINT fk_ocorrencia_morador FOREIGN KEY (id_morador) REFERENCES MORADORES(id_morador)
- CONSTRAINT fk_ocorrencia_funcionario FOREIGN KEY (id_funcionario) REFERENCES FUNCIONARIOS(id_funcionario)

## 13. FORNECEDORES
- **id_fornecedor**: INT [PK, AUTO_INCREMENT]
- **razao_social**: VARCHAR(100) [NOT NULL]
- **cnpj**: VARCHAR(14) [NOT NULL, UNIQUE]
- **telefone**: VARCHAR(20)
- **email**: VARCHAR(100)

## 14. SERVICOS
- **id_servico**: INT [PK, AUTO_INCREMENT]
- **descricao**: VARCHAR(100) [NOT NULL]
- **periodicidade**: VARCHAR(50)

## 15. CONTRATOS
- **id_contrato**: INT [PK, AUTO_INCREMENT]
- **id_fornecedor**: INT [FK, NOT NULL]
- **id_servico**: INT [FK, NOT NULL]
- **data_inicio**: DATE [NOT NULL]
- **data_fim**: DATE
- **valor**: DECIMAL(10,2) [NOT NULL]
- **status**: ENUM('Ativo', 'Encerrado', 'Cancelado') [DEFAULT 'Ativo']
- CONSTRAINT fk_contrato_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES FORNECEDORES(id_fornecedor)
- CONSTRAINT fk_contrato_servico FOREIGN KEY (id_servico) REFERENCES SERVICOS(id_servico)

### Observações sobre Domínios e Restrições:

1. **Campos Numéricos**:
   - Valores monetários: DECIMAL(10,2) para suportar valores até 99.999.999,99
   - Metragem: DECIMAL(6,2) para suportar valores até 9.999,99m²

2. **Campos de Texto**:
   - Nomes e razões sociais: VARCHAR(100)
   - Descrições curtas: VARCHAR(50)
   - Documentos (CPF/CNPJ): tamanhos fixos (11/14)
   - Telefones: VARCHAR(20) para suportar diferentes formatos

3. **Datas e Horários**:
   - Datas simples: DATE
   - Data/hora com precisão: DATETIME
   - Valores default: CURRENT_DATE ou CURRENT_TIMESTAMP

4. **Enumerações**:
   - Status de reservas: ['Pendente', 'Confirmada', 'Cancelada']
   - Status de faturas: ['Pendente', 'Paga', 'Atrasada']
   - Status de ocorrências: ['Aberta', 'Em Andamento', 'Resolvida', 'Cancelada']
   - Prioridade de ocorrências: ['Baixa', 'Média', 'Alta']
   - Status de contratos: ['Ativo', 'Encerrado', 'Cancelado']

5. **Chaves e Índices**:
   - Todas as tabelas possuem chave primária auto-incrementável
   - Chaves estrangeiras com ON DELETE RESTRICT por padrão
   - Índices únicos em campos como CPF, CNPJ e placa de veículo

6. **Valores Default**:
   - Campos booleanos: DEFAULT TRUE/FALSE
   - Campos de status: primeiro valor da enumeração
   - Datas de registro: data/hora atual