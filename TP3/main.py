'''
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

    Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: # Exemplo
Out: <h1>Exemplo</h1>
'''
import re

def cabecalhos_to_html(markdown):
# Define a regular expression pattern to match the markdown headers
                    pattern = r'^(#{1,3})\s(.+)$'
                    html = re.sub(pattern,r'<h{len(\1)}>{\2}</h{\3}>', markdown)
                    # Return the converted HTML
                    return html


'''

    Bold: pedaços de texto entre "**":

In: Este é um **exemplo** ...
Out: Este é um <b>exemplo</b> ...
'''
def bold_to_html(markdown):
       # Define a regular expression pattern to match the markdown bolds
       pattern = r'\*\*(.+)\*\*'
       html = re.sub(pattern,r'<b>{\1}</b>', markdown)
       # Return the converted HTML
       return html