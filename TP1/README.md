# PL2024

## Unidade Curricular

**Nome**: Processamento de Linguagens

**Sigla**: PL

**Ano**: 2024

**TPC**: TPC1

A função `parsingficheiro()` lê um ficheiro CSV chamado 'emd.csv', onde cada linha representa dados de um atleta. Os dados são processados e organizados num dicionário onde a chave é o segundo elemento de cada linha (presumivelmente um identificador único) e o valor é uma lista com todos os dados dessa linha.

A função `listarModalidade(dados)` percorre o dicionário de dados e cria um conjunto de todas as modalidades desportivas presentes nos dados, retornando este conjunto ordenado alfabeticamente.

A função `percentagemAptos(dados)` calcula a percentagem de atletas aptos e inaptos para a prática desportiva. Ela percorre os dados, contabilizando o número de atletas aptos e inaptos e calcula as percentagens com base no número total de atletas.

A função `distribuicaoAtletas(dados)` analisa a idade de cada atleta e determina o seu escalão etário, considerando intervalos de 5 anos. Ela retorna um dicionário onde as chaves são os intervalos de idade (por exemplo, '30 - 34') e os valores são o número de atletas dentro desse intervalo.

Por fim, na função `main()`, são invocadas as funções anteriores para processar os dados e gerar os resultados desejados, que são impressos no terminal.

## Aluno

**Nome**: Bruno Alexandre Carvalho Silva

**ID** : a100828
