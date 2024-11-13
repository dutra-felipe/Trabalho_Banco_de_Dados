```SQL

-- 1. UNIDADES
INSERT INTO UNIDADES (bloco, numero, metragem, vagas_garagem)
VALUES ('A', '103', 90.00, 2),
       ('B', '202', 70.30, 1),
       ('C', '301', 95.00, 2),
       ('C', '302', 80.00, 1),
       ('D', '401', 60.00, 1);

-- 2. MORADORES
INSERT INTO MORADORES (id_unidade, nome, cpf, email, telefone, data_cadastro, ativo)
VALUES (3, 'Carlos Pereira', '34567890123', 'carlos.pereira@example.com', '(11) 98888-1111', CURRENT_DATE, TRUE),
       (4, 'Fernanda Lima', '45678901234', 'fernanda.lima@example.com', '(11) 97777-2222', CURRENT_DATE, TRUE),
       (5, 'Lucas Souza', '56789012345', 'lucas.souza@example.com', '(11) 96666-3333', CURRENT_DATE, TRUE),
       (1, 'Juliana Mendes', '67890123456', 'juliana.mendes@example.com', '(11) 95555-4444', CURRENT_DATE, TRUE),
       (2, 'Ricardo Silva', '78901234567', 'ricardo.silva@example.com', '(11) 94444-5555', CURRENT_DATE, FALSE);

-- 3. VEICULOS
INSERT INTO VEICULOS (id_unidade, placa, modelo, cor)
VALUES (3, 'DEF1234', 'Ford Fiesta', 'Branco'),
       (4, 'GHI5678', 'Chevrolet Onix', 'Azul'),
       (5, 'JKL9101', 'Hyundai HB20', 'Vermelho'),
       (1, 'MNO2345', 'Nissan Versa', 'Preto'),
       (2, 'PQR3456', 'Volkswagen Golf', 'Cinza');

-- 4. VISITANTES
INSERT INTO VISITANTES (nome, documento, telefone, data_cadastro)
VALUES ('Renato Araujo', 'RG3456789', '(11) 93333-6666', CURRENT_TIMESTAMP),
       ('Daniela Costa', 'RG4567890', '(11) 92222-7777', CURRENT_TIMESTAMP),
       ('Thiago Martins', 'RG5678901', '(11) 91111-8888', CURRENT_TIMESTAMP),
       ('Patricia Gomes', 'RG6789012', '(11) 90000-9999', CURRENT_TIMESTAMP),
       ('André Silva', 'RG7890123', '(11) 98888-0000', CURRENT_TIMESTAMP);

-- 5. AUTORIZACOES_VISITANTES
INSERT INTO AUTORIZACOES_VISITANTES (id_morador, id_visitante, data_autorizacao, data_validade)
VALUES (3, 3, CURRENT_TIMESTAMP, '2024-12-31'),
       (4, 4, CURRENT_TIMESTAMP, '2024-11-30'),
       (5, 5, CURRENT_TIMESTAMP, '2025-01-15'),
       (1, 1, CURRENT_TIMESTAMP, '2024-12-01'),
       (2, 2, CURRENT_TIMESTAMP, '2024-12-15');

-- 6. AREAS_COMUNS
INSERT INTO AREAS_COMUNS (nome, capacidade, taxa_uso, requer_reserva)
VALUES ('Quadra de Esportes', 30, 0.00, FALSE),
       ('Academia', 20, 0.00, FALSE),
       ('Sauna', 5, 50.00, TRUE),
       ('Salão de Jogos', 15, 0.00, FALSE);

-- 7. RESERVAS
INSERT INTO RESERVAS (id_morador, id_area, data_hora_inicio, data_hora_fim, valor, status)
VALUES (3, 1, '2024-11-22 14:00:00', '2024-11-22 16:00:00', 0.00, 'Confirmada'),
       (4, 3, '2024-11-23 17:00:00', '2024-11-23 19:00:00', 50.00, 'Pendente'),
       (5, 4, '2024-11-24 15:00:00', '2024-11-24 18:00:00', 0.00, 'Cancelada'),
       (1, 2, '2024-11-25 10:00:00', '2024-11-25 12:00:00', 0.00, 'Confirmada'),
       (2, 1, '2024-11-26 09:00:00', '2024-11-26 11:00:00', 0.00, 'Pendente');

-- 8. TAXAS
INSERT INTO TAXAS (descricao, valor_base, recorrente)
VALUES ('Taxa de Limpeza', 150.00, FALSE),
       ('Taxa de Manutenção', 300.00, TRUE),
       ('Fundo de Reserva', 200.00, TRUE);

-- 9. FATURAS
INSERT INTO FATURAS (id_unidade, data_vencimento, valor_total, status)
VALUES (3, '2024-12-10', 650.00, 'Pendente'),
       (4, '2024-12-10', 700.00, 'Atrasada'),
       (5, '2024-12-10', 500.00, 'Pendente'),
       (1, '2024-12-05', 800.00, 'Paga'),
       (2, '2024-12-05', 600.00, 'Paga');

-- 10. ITENS_FATURA
INSERT INTO ITENS_FATURA (id_fatura, id_taxa, valor)
VALUES (1, 1, 150.00),
       (1, 2, 300.00),
       (1, 3, 200.00),
       (2, 1, 150.00),
       (2, 3, 200.00),
       (3, 2, 300.00),
       (3, 3, 200.00);

-- 11. FUNCIONARIOS
INSERT INTO FUNCIONARIOS (nome, cargo, data_admissao, ativo)
VALUES ('Pedro Rocha', 'Síndico', '2020-06-01', TRUE),
       ('Cláudia Mota', 'Auxiliar de Limpeza', '2021-08-15', TRUE),
       ('Roberto Nunes', 'Manutenção', '2019-11-22', TRUE),
       ('Silvia Souza', 'Segurança', '2022-02-10', TRUE),
       ('Luciana Silva', 'Jardineira', '2021-05-12', TRUE);

-- 12. OCORRENCIAS
INSERT INTO OCORRENCIAS (id_morador, id_funcionario, data_registro, descricao, status, prioridade)
VALUES (3, 2, CURRENT_TIMESTAMP, 'Problema na área de lazer', 'Aberta', 'Média'),
       (4, 3, CURRENT_TIMESTAMP, 'Barulho excessivo no bloco B', 'Em Andamento', 'Alta'),
       (5, NULL, CURRENT_TIMESTAMP, 'Manutenção elétrica necessária', 'Aberta', 'Alta'),
       (1, 4, CURRENT_TIMESTAMP, 'Porta de entrada quebrada', 'Resolvida', 'Média'),
       (2, NULL, CURRENT_TIMESTAMP, 'Infiltração na parede', 'Aberta', 'Baixa');

-- 13. FORNECEDORES
INSERT INTO FORNECEDORES (razao_social, cnpj, telefone, email)
VALUES ('Segurança e Cia', '34567890000177', '(11) 3666-7788', 'contato@segurancaecia.com.br'),
       ('Jardinagem Verde Ltda', '45678900000155', '(11) 3999-8877', 'contato@jardiverde.com.br'),
       ('Limpeza Urbana SA', '56789000000144', '(11) 3222-6644', 'atendimento@limpezaurbana.com.br');

-- 14. SERVICOS
INSERT INTO SERVICOS (descricao, periodicidade)
VALUES ('Segurança 24h', 'Diário'),
       ('Limpeza Externa', 'Quinzenal'),
       ('Jardinagem', 'Mensal');

-- 15. CONTRATOS
INSERT INTO CONTRATOS (id_fornecedor, id_servico, data_inicio, data_fim, valor, status)
VALUES (3, 1, '2024-01-01', '2024-12-31', 25000.00, 'Ativo'),
       (1, 2, '2024-02-01', '2024-12-31', 10000.00, 'Ativo'),
       (2, 3, '2024-03-01', '2024-12-31', 8000.00, 'Encerrado');
```