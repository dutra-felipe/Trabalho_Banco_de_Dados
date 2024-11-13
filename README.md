# Sistema de Gestão de Condomínio

## Visão Geral
Este projeto implementa um sistema de banco de dados para a gestão de um condomínio. Ele permite gerenciar unidades, moradores, visitantes, funcionários, veículos, áreas comuns, reservas, cobranças e contratos de serviços de forma organizada e eficiente. O banco de dados foi estruturado em conformidade com as práticas de normalização até a 3ª Forma Normal.

## Estrutura do Projeto
- **Tabelas de Dados**: O sistema contém diversas tabelas relacionadas entre si por chaves estrangeiras, mantendo a integridade e consistência dos dados.
- **Scripts SQL**: Scripts para criação, inserção (DML), consultas e *views* para gerar relatórios.

## Tabelas
O sistema é composto pelas seguintes tabelas principais:

1. **UNIDADES** - Representa cada unidade do condomínio, com informações como bloco, número, metragem e vagas de garagem.
2. **MORADORES** - Armazena os dados dos moradores de cada unidade, incluindo nome, CPF, contato e status.
3. **VEICULOS** - Lista os veículos associados às unidades do condomínio.
4. **VISITANTES** - Armazena dados de visitantes cadastrados no condomínio.
5. **AUTORIZACOES_VISITANTES** - Controle de autorizações de acesso de visitantes.
6. **AREAS_COMUNS** - Define as áreas comuns disponíveis no condomínio e sua capacidade.
7. **RESERVAS** - Informações sobre as reservas feitas pelos moradores nas áreas comuns.
8. **TAXAS** - Descrição das taxas e valores associados ao condomínio.
9. **FATURAS** - Faturas geradas para cada unidade, incluindo valor total e status de pagamento.
10. **ITENS_FATURA** - Itens que compõem cada fatura, vinculando taxas a uma fatura específica.
11. **FUNCIONARIOS** - Cadastro dos funcionários do condomínio.
12. **OCORRENCIAS** - Relatório de ocorrências registradas pelos moradores e funcionários.
13. **FORNECEDORES** - Dados dos fornecedores de serviços.
14. **SERVICOS** - Lista dos serviços fornecidos ao condomínio.
15. **CONTRATOS** - Contratos com fornecedores e status.
