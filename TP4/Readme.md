# PL2024

## Unidade Curricular

**Nome**: Processamento de Linguagens

**Sigla**: TP4

**Ano**: 2024



##Explicação do Código

Este script Python utiliza o módulo `ply.lex` para criar um lexer que reconhece tokens em uma string de entrada no formato  por exemplo assim `id=1 nome=maria salario=1000.00`.

Os tokens são definidos na lista `tokens`, que inclui `'id'`, `'nome'` e `'salario'`.

Para cada token, há uma regra de expressão regular que o identifica na entrada. Por exemplo, `t_id` corresponde a um padrão que identifica o token `'id'` seguido de um número. Similarmente, `t_nome` identifica o token `'nome'` seguido de uma sequência de caracteres alfanuméricos. `t_salario` identifica o token `'salario'` seguido de um número, opcionalmente seguido por uma parte decimal.

Além disso, há uma função `t_NUMBER` que converte sequências de dígitos em números inteiros.

A função `t_newline` rastreia as mudanças de linha na entrada.

Os caracteres ignorados, como espaços e tabulações, são definidos na variável `t_ignore`.

A função `t_error` lida com erros de caracteres não reconhecidos.

Finalmente, o lexer é construído e testado com uma string de entrada que contém um exemplo de dados. Os tokens reconhecidos são impressos.
