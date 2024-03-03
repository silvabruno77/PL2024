'''
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

    Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: # Exemplo
Out: <h1>Exemplo</h1>
'''
import re

def cabecalhos_to_html(markdown):
                    pattern = r'^(#{1,3})\s(.+)$'
                    html = re.sub(pattern,r'<h{len(\1)}>{\2}</h{\3}>', markdown)
                    return html


'''

    Bold: pedaços de texto entre "**":

In: Este é um **exemplo** ...
Out: Este é um <b>exemplo</b> ...
'''
def bold_to_html(markdown):
       pattern = r'\*\*(.+)\*\*'
       html = re.sub(pattern,r'<b>{\1}</b>', markdown)
       return html


'''


    Itálico: pedaços de texto entre "*":

In: Este é um *exemplo* ...
Out: Este é um <i>exemplo</i> ...

'''

def italic_to_html(markdown):
         pattern = r'\*(.+)\*'
         html = re.sub(pattern,r'<i>{\1}</i>', markdown)
         return html

'''

    Lista numerada:

In:
1. Primeiro item
2. Segundo item
3. Terceiro item
Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
'''
def lista_numerada_to_html(markdown):
    pattern = r'^(\d+\.\s.+)$'
    html = re.sub(pattern,r'<ol>\n<li>{\1}</li>\n</ol>', markdown)
    return html

'''


    Link: [texto](endereço URL)

In: Como pode ser consultado em [página da UC](http://www.uc.pt)
Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

'''

def link_to_html(markdown):
    pattern = r'\[(.+)\]\((.+)\)'
    html = re.sub(pattern,r'<a href="{\2}">{\1}</a>', markdown)
    return html


'''


    Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
'''

def imagem_to_html(markdown):
    pattern = r'!\[(.+)\]\((.+)\)'
    html = re.sub(pattern,r'<img src="{\2}" alt="{\1}"/>', markdown)
    return html


