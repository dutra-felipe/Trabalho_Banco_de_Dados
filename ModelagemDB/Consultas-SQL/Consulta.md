1. Consultas Simples

- a) Listar todas as unidades com seus respectivos moradores

```SQL
SELECT u.bloco, u.numero, m.nome AS morador, m.cpf, m.telefone
FROM UNIDADES u
LEFT JOIN MORADORES m ON u.id_unidade = m.id_unidade
ORDER BY u.bloco, u.numero;
```

- b) Consultar todas as reservas feitas por moradores, incluindo a área comum reservada e o status

```SQL
SELECT r.id_reserva, m.nome AS morador, ac.nome AS area_comum, r.data_hora_inicio, r.data_hora_fim, r.valor, r.status
FROM RESERVAS r
JOIN MORADORES m ON r.id_morador = m.id_morador
JOIN AREAS_COMUNS ac ON r.id_area = ac.id_area
ORDER BY r.data_hora_inicio DESC;
```

- c) Listar todas as ocorrências, incluindo o morador que registrou e o funcionário responsável (se houver)

```SQL
SELECT o.id_ocorrencia, m.nome AS morador, f.nome AS funcionario, o.data_registro, o.descricao, o.status, o.prioridade
FROM OCORRENCIAS o
JOIN MORADORES m ON o.id_morador = m.id_morador
LEFT JOIN FUNCIONARIOS f ON o.id_funcionario = f.id_funcionario
ORDER BY o.data_registro DESC;
```

2. Relatórios

- a) Relatório de faturamento total por unidade com status da fatura

```SQL
SELECT u.bloco, u.numero, SUM(f.valor_total) AS total_faturado, f.status
FROM FATURAS f
JOIN UNIDADES u ON f.id_unidade = u.id_unidade
GROUP BY u.bloco, u.numero, f.status
ORDER BY u.bloco, u.numero;
```

- b) Relatório de moradores e seus veículos

```SQL
SELECT m.nome AS morador, m.telefone, v.placa, v.modelo, v.cor
FROM MORADORES m
JOIN VEICULOS v ON m.id_unidade = v.id_unidade
ORDER BY m.nome;
```

- c) Consultar todas as autorizações de visitantes válidas até uma data específica

```SQL
SELECT a.id_autorizacao, m.nome AS morador, v.nome AS visitante, a.data_autorizacao, a.data_validade
FROM AUTORIZACOES_VISITANTES a
JOIN MORADORES m ON a.id_morador = m.id_morador
JOIN VISITANTES v ON a.id_visitante = v.id_visitante
WHERE a.data_validade >= '2024-12-01'
ORDER BY a.data_autorizacao DESC;
```

3. Views

- a) View para as ocorrências abertas e em andamento

```SQL
CREATE VIEW vw_ocorrencias_abertas AS
SELECT o.id_ocorrencia, m.nome AS morador, f.nome AS funcionario, o.data_registro, o.descricao, o.status, o.prioridade
FROM OCORRENCIAS o
JOIN MORADORES m ON o.id_morador = m.id_morador
LEFT JOIN FUNCIONARIOS f ON o.id_funcionario = f.id_funcionario
WHERE o.status IN ('Aberta', 'Em Andamento');
```

- b) View para faturamento por unidade

```SQL
CREATE VIEW vw_faturamento_por_unidade AS
SELECT u.bloco, u.numero, SUM(f.valor_total) AS total_faturado
FROM FATURAS f
JOIN UNIDADES u ON f.id_unidade = u.id_unidade
GROUP BY u.bloco, u.numero;
```

- c) View de áreas comuns que requerem reserva

```SQL
CREATE VIEW vw_areas_requer_reserva AS
SELECT nome, capacidade, taxa_uso
FROM AREAS_COMUNS
WHERE requer_reserva = TRUE;
```

4. Consultas Mais Complexas

- a) Total de reservas e valor arrecadado por área comum

```SQL
SELECT ac.nome AS area_comum, COUNT(r.id_reserva) AS total_reservas, SUM(r.valor) AS valor_arrecadado
FROM RESERVAS r
JOIN AREAS_COMUNS ac ON r.id_area = ac.id_area
GROUP BY ac.nome
ORDER BY valor_arrecadado DESC;
```

- b) Consultar moradores com status de fatura "Atrasada"

```SQL
SELECT m.nome AS morador, m.cpf, u.bloco, u.numero, f.data_vencimento, f.valor_total
FROM MORADORES m
JOIN UNIDADES u ON m.id_unidade = u.id_unidade
JOIN FATURAS f ON u.id_unidade = f.id_unidade
WHERE f.status = 'Atrasada'
ORDER BY f.data_vencimento DESC;
```

- c) Consultar contratos ativos com fornecedores e valor total de contratos

```SQL
SELECT f.razao_social AS fornecedor, s.descricao AS servico, c.data_inicio, c.data_fim, c.valor, c.status
FROM CONTRATOS c
JOIN FORNECEDORES f ON c.id_fornecedor = f.id_fornecedor
JOIN SERVICOS s ON c.id_servico = s.id_servico
WHERE c.status = 'Ativo'
ORDER BY c.data_inicio;
```

5. View de Moradores Ativos e Veículos Associados

```SQL
CREATE VIEW vw_moradores_veiculos AS
SELECT m.nome AS morador, m.cpf, v.placa, v.modelo, v.cor
FROM MORADORES m
LEFT JOIN VEICULOS v ON m.id_unidade = v.id_unidade
WHERE m.ativo = TRUE;
```