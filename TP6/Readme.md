# PL2024

## Unidade Curricular

**Nome**: Processamento de Linguagens

**Sigla**: TP6

**Ano**: 2024

# Objetivo com a Gramática

`?a`

`b = a * 2 / (27 - 3)`

`!a + b`

`c = a * b / (a / b)`


# Explicação da Gramática

A gramática fornecida define uma linguagem de expressões e atribuições de variáveis. Abaixo está uma descrição detalhada de cada regra e como interpretar a gramática.

## Regras da Gramática

A regra inicial, S, pode expandir-se em três formas diferentes:
- `S -> ? variable`: Permite uma consulta de uma variável (por exemplo, `?a`).
- `S -> ! Exprex`: Permite a execução de uma expressão (por exemplo, `!a+b`).
- `S -> variable = Expr`: Permite a atribuição de uma expressão a uma variável (por exemplo, `b = a*2/(27-3)`).

Esta regra define uma expressão complexa:
- `Exprex -> Exprex2 Oper`: Uma expressão complexa é composta por uma `Exprex2` seguida de uma `Oper`.

Esta regra define os operadores disponíveis para `Exprex`:
- `Oper -> + Exprex`: Soma de `Exprex2` com outra `Exprex`.
- `Oper -> - Exprex`: Subtração de `Exprex2` com outra `Exprex`.
- `Oper -> &`: Vazio

Esta regra define uma expressão intermediária:
- `Exprex2 -> Exprex3 Oper2`: Uma `Exprex2` é composta por uma `Exprex3` seguida de um `Oper2`.

Esta regra define os operadores disponíveis para `Exprex2`:
- `Oper2 -> * Expr +`: Multiplicação de `Exprex3` com uma `Expr`.
- `Oper2 -> &`: Vazio

Esta regra define uma expressão simples:
- `Exprex3 -> ( Exprex )`: Uma expressão entre parênteses.
- `Exprex3 -> id`: Um id.
- `Exprex3 -> num`: Um número.

## Conclusão

A gramática permite a definição de consultas de variáveis, execução de expressões e atribuições de valores a variáveis. As expressões podem ser compostas por operações aritméticas e lógicas, utilizando variáveis e números, com a possibilidade de agrupamento usando parênteses.
