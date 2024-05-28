# PL2024

## Unidade Curricular

**Nome**: Processamento de Linguagens

**Sigla**: TP5

**Ano**: 2024

# Objetivo

Simulação da máquina de vending, explicação em pdf

# Explicação do Código

O código fornecido é dividido em duas funções principais: `analisarMoedasLista` e `analisadorMoeda`. A seguir, explico cada uma delas em detalhe, em Português de Portugal.

## Função `analisarMoedasLista`

Esta função `analisarMoedasLista` tem como objetivo analisar uma lista de moedas e identificar a sua denominação (euros, cêntimos ou um ponto). 

- **Entrada:** Uma lista de strings onde cada string representa uma moeda ou um ponto, por exemplo, `["1e", "20c", "5c", "5c", "."]`.
- **Processo:**
  - Itera sobre cada elemento da lista.
  - Verifica o último carácter da string (`moeda[-1]`):
    - Se for `"e"`, imprime a parte numérica da moeda (o valor antes do "e").
    - Se for `"c"`, imprime a parte numérica da moeda (o valor antes do "c").
    - Se for `"."`, imprime um ponto.
    - Caso contrário, imprime "Moeda inválida".
- **Saída:** Não retorna nada, apenas imprime o valor ou uma mensagem de moeda inválida.

## Função `analisadorMoeda`

A função `analisadorMoeda` utiliza a biblioteca `ply.lex` para criar um analisador léxico (lexer) que reconhece diferentes tipos de moedas.

- **Tokens:** Define um conjunto de tokens (`tokens`) que incluem "euros", "centimos" e "ponto".
- **Expressões Regulares:** Utiliza expressões regulares para identificar euros, cêntimos e pontos.
  - `t_ponto = r'\.'` reconhece um ponto.
  - `t_euros = r'\d+e'` reconhece um número seguido de um "e" (representando euros).
  - `t_centimos = r'\d+c'` reconhece um número seguido de um "c" (representando cêntimos).
- **Funções Auxiliares:**
  - `t_error(t)`: Função de erro que imprime um carácter ilegal e avança para o próximo.
  - `t_euros(t)`: Converte a string correspondente a euros para um inteiro e imprime-o.
  - `t_centimos(t)`: Converte a string correspondente a cêntimos para um inteiro e imprime-o.
- **Processo:**
  - Concatena a lista de moedas numa única string (`ListamoedaString`).
  - Inicializa o lexer com a string de entrada.
  - Itera sobre os tokens reconhecidos e imprime-os.

### Possíveis Melhorias e Funcionalidades Extras:

- **Adicionar Produtos:** Permitir adicionar novos produtos ou atualizar o stock existente.
- **Gerir Erros:** Lidar com casos de produtos inexistentes ou stock vazio.
- **Persistência de Dados:** Garantir que o stock é salvo e carregado corretamente no arranque e desligamento da máquina.

Este exemplo ilustra como uma máquina de vending pode ser simulada e os diferentes cenários que devem ser contemplados.
