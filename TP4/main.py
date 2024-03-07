import re
import os
import sys
import ply.lex as lex


# List of token names.   This is always required
tokens = (
   'id',
   'nome',
   'salario'
)

# Regular expression rules for simple tokens
t_id    = r'id=\d+'
t_nome   = r'nome=\w+'
t_salario   = r'salario=\d+'
#t_DIVIDE  = r'/'
#t_LPAREN  = r'\('
#t_RPAREN  = r'\)'


# A regular expression rule with some action code
# Note addition of self parameter since we're in a class
def t_NUMBER(self, t):
   r'\d+'
   t.value = int(t.value)
   return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
id=1 nome=joao salario=1000
'''

# Give the lexer some input
lexer.input(data)

for tok in lexer:
    print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)