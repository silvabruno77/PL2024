# PL2024

## Unidade Curricular

**Nome**: Processamento de Linguagens

**Sigla**: TPC2

**Ano**: 2024


Este código é um pequeno programa em Python que converte texto escrito em Markdown para HTML, seguindo algumas regras específicas. Vou resumir cada parte:

    Cabeçalhos: Esta função procura por linhas iniciadas com um ou mais símbolos '#' seguidos de texto. Converte essas linhas para HTML, onde a quantidade de '#' determina o nível do cabeçalho (<h1>, <h2>, <h3>), e o texto é colocado dentro das tags de cabeçalho correspondentes.

    Negrito (Bold): Procura por pedaços de texto envolvidos por dois asteriscos "**". Substitui esses pedaços pelo texto envolvido em tags HTML de negrito (<b>).

    Itálico: Similar ao negrito, mas procura por pedaços de texto entre um único asterisco "*". Substitui esses pedaços pelo texto envolvido em tags HTML de itálico (<i>).

    Lista Numerada: Procura por linhas que iniciam com um número seguido de um ponto e espaço. Converte essas linhas em uma lista numerada HTML (<ol>) onde cada item é envolvido por tags <li>.

    Link: Procura por um texto entre colchetes, seguido de um endereço URL entre parênteses. Converte isso em uma tag HTML de link (<a>) onde o texto é o conteúdo do link e o endereço URL é o destino.

    Imagem: Similar ao link, mas procura por um texto alternativo entre colchetes e o caminho para a imagem entre parênteses. Converte isso em uma tag HTML de imagem (<img>) onde o texto alternativo é o atributo "alt" e o caminho para a imagem é o atributo "src".



## Aluno

**Nome**: Bruno Alexandre Carvalho Silva

**ID** : a100828
