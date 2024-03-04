'''

Somador on/off
Somador on/off: criar o programa em Python

    Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
    Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
    Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
    Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

'''
def somador_on_off(texto):
    somar = False
    resultado = 0
    for c in texto:
        if c.lower() == 'o':
            somar = False
        elif c.lower() == 'n':
            somar = True
        elif c.isdigit() and somar:
            resultado += int(c)
        elif c == '=':
            return resultado
    return resultado




"""
Com expreções regulares o somador_on_off pode ser escrito da seguinte forma:
Foi dado um exemplo na aula, usei como base
"""
import re
def somador_on_off_re(texto):
    texto = ''' 
    Este é apenas 1 texto demonstrativo.
    Amanhã, 2023-03-07, tens de ir visitar o teu amigo.
    Até agora totalizamos: =
    ofF
    Agora já não está a somar os números: 1, 2, ...
    On, ligou-se outra vez, cuidado com o 1, 2, 3 ...
    Chegamos ao fim com =
    '''

    token_specification = [
            ('INT', r'(\+|-)?\d+'),             
            ('ON',  r'(?i:on)'),             
            ('OFF', r'(?i:off)'),
            ('EQ', r'='),
            ('SKIP', r'\s+'),
            ('UNKNOWN', r'.')
        ]

    mypattern = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)