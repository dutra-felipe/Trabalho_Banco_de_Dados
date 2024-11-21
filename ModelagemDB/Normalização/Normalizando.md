# Processo de Normalização

## 1ª Forma Normal (1FN)
- Eliminar grupos repetitivos
- Identificar a chave primária de cada tabela
- Garantir que cada atributo seja atômico

### Transformações Realizadas:
1. **Contatos de Moradores**
   - Antes: Tabela MORADORES com múltiplos telefones
   - Depois: Campo telefone único e atômico

2. **Veículos por Unidade**
   - Antes: Lista de veículos dentro da tabela UNIDADES
   - Depois: Tabela VEICULOS separada com FK para UNIDADES

3. **Autorizações de Visitantes**
   - Antes: Lista de visitantes autorizados na tabela MORADORES
   - Depois: Tabela AUTORIZACOES_VISITANTES separada

## 2ª Forma Normal (2FN)
- Já estar na 1FN
- Remover dependências parciais da chave primária

### Transformações Realizadas:
1. **Taxas e Faturas**
   - Antes: Informações de taxa na tabela FATURAS
   - Depois: Tabela TAXAS separada e ITENS_FATURA para relacionamento

2. **Reservas e Áreas Comuns**
   - Antes: Dados da área comum na tabela RESERVAS
   - Depois: Tabela AREAS_COMUNS separada

3. **Contratos e Serviços**
   - Antes: Descrição do serviço na tabela CONTRATOS
   - Depois: Tabela SERVICOS separada

## 3ª Forma Normal (3FN)
- Já estar na 2FN
- Eliminar dependências transitivas

### Transformações Realizadas:
1. **Endereço da Unidade**
   - Antes: Bloco determina setor do condomínio
   - Depois: Atributos independentes

2. **Cálculo de Valores**
   - Antes: Valor total calculado em FATURAS
   - Depois: Calculado a partir de ITENS_FATURA

3. **Status de Pagamento**
   - Antes: Status derivado de outras informações
   - Depois: Status explícito com regras de negócio

## Resultado da Normalização:
1. Dados não redundantes
2. Integridade referencial mantida
3. Facilidade de manutenção
4. Consistência dos dados
5. Eliminação de anomalias de atualização