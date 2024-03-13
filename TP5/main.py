## Problema de vending machine
import time
import re
import ply.lex as lex


stock =[
    {"cod": "A1", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    {"cod": "A2", "nome": "CoCa-Cola", "quant": 5, "preco": 1.2},
    {"cod": "A3", "nome": "Café", "quant": 10, "preco": 0.5},
]

# Futuramente ler do json
if (True):
    tempoatual = time.strftime("%Y-%m-%d", time.localtime())
    print(rf"{tempoatual}, Stock carregado, Estado atualizado.")
    print("Bom dia. Estou disponível para atender o seu pedido.")

# Listar produtos do stock
def listar_stock():
    print("Código | Nome | Quantidade | Preço")
    for produto in stock:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']}")

saldo_Total = 0
# Adicionar dinheiro
def adicionar_dinheiro(dinheiro):
        dinheiro += float(input())
        saldo_Total += dinheiro
        print(f"Saldo = {saldo_Total}")

loop = True

def tratarResultado(argumento):
    tokens = (
        'MOEDA',
        'SELECIONAR',
        'LISTAR',
    )
    t_SELECIONAR = r'SELECIONAR'
    t_LISTAR = r'LISTAR'
    t_ignore = ' \t\n'
    def t_MOEDA(t):
        r'MOEDA\s+(?:\d+[ec],\s*)*'
        t.value = t.value.split()
        print(t.value)
        return t

    def t_error(t):
        print(f"Carácter ilegal {t.value[0]}")
        t.lexer.skip(1)

    lexer = lex.lex()
    lexer.input(argmumento)

    while tok := lexer.token():
        print(tok)




while loop:
    argmumento = input()
    ## Ou é Moeda ou SELECIONAR ou LISTAR
    resultado = re.split(r'MOEDA|SELECIONAR|LISTAR', argmumento)
    tratarResultado(argmumento) 




