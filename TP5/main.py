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


def tratarResultado(argumento):
    print(argumento)
    tokens = (
        'MOEDA',
        'SELECIONAR',
        'LISTAR',
        'Saldo'
    )
    t_LISTAR = r'LISTAR'
    t_ignore = ' \t\n'

    def t_MOEDA(t):
        r'MOEDA\s+((\d+[ec],\s?)+)\s+((\d+[ec]\s*)+\.)$'
        t.value = t.value.split()
        analisarMoedasLista(t.value[1:-1])
        print(t.value)
        return t

    def t_error(t):
        print(f"Carácter ilegal {t.value[0]}")
        t.lexer.skip(1)
    
    def t_Saldo(t):
        r'Saldo'
        print(saldo_Total)
        return t
    

    def t_SELECIONAR(t):
        #SELECIONAR A23
        r'SELECIONAR\s+([A-Z]\d)$'
        print("Valor do token " + t.value)
        produto = re.findall(r'([A-Z]\d)', t.value)
        if stockDisponivel(produto[0]) == 0:
            print("Produto indisponível")
        else:
            comprarproduto(produto[0])
        return t

    lexer = lex.lex()
    lexer.input(argmumento)

    while tok := lexer.token():
        print(tok)

def analisarMoedasLista(Listamoeda):
    #MOEDA 1e, 20c, 5c, 5c .
    global saldo_Total
    for moeda in Listamoeda:
        print(moeda)
        if moeda[-1] == "e":
            print("Moeda de euros")
            saldo_Total += int(moeda[:-1])
            print(moeda[:-1])
        if moeda[-2] == "e":
            print("Moeda de euros")
            saldo_Total += int(moeda[:-2])
        if moeda[-1] == "c":
            print("Moeda de centimos")
            saldo_Total += int(moeda[:-1]) * 0.01
        elif moeda[-2] == "c":
            print("Moeda de centimos")
            saldo_Total += int(moeda[:-2]) * 0.01
        elif moeda[-1] == ".":
            print("Ponto")
            print(moeda[:-1])
        else:
            print("Moeda inválida")
        # maq: Saldo = 1e30c
        saldoString = SaldoParaString(saldo_Total)
        print(f"Saldo = {saldoString}")


def SaldoParaString(saldo):
    ## 1.3 -> 1e30c
    print("Saldo total " + str (saldo))
    saldoString = ""
    euros = int(saldo)
    print("Saldo em euros " + str(euros))
    centimos = int((saldo - euros) * 100)
    saldoString += f"{euros}e"
    saldoString += f"{centimos}c"
    return saldoString



##         r'MOEDA\s+(((\d+[ec],\s?)+)\s+)((\d+[ec]\s*)+\.)$'


def stockDisponivel(cod):
    for produto in stock:
        if produto['cod'] == cod:
            return produto['quant']
    return 0

def comprarproduto(cod):
    global saldo_Total
    for produto in stock:
        if produto['cod'] == cod:
            if produto['preco'] <= saldo_Total:
                produto['quant'] -= 1
                saldo_Total -= produto['preco']
                # maq: Pode retirar o produto dispensado "água 0.5L"
                print(f"maq: Pode retirar o produto dispensado {produto['nome']}")
                # maq: Saldo = 60c
                print(f"maq: Saldo = {SaldoParaString(saldo_Total)}")
                return
            else:
                print("maq: Saldo insufuciente para satisfazer o seu pedido")
                #maq: Saldo = 60c; Pedido = 70c
                print(f"maq: Saldo = {SaldoParaString(saldo_Total)}; Pedido = {SaldoParaString(produto['preco'])}")
                return
    print("Produto não encontrado")


loop = True
while loop:
    argmumento = input()
    ## Ou é Moeda ou SELECIONAR ou LISTAR
    resultado = re.split(r'MOEDA|SELECIONAR|LISTAR', argmumento)
    tratarResultado(argmumento) 




