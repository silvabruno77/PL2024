


def analisarMoedasLista(Listamoeda):
    #MOEDA 1e, 20c, 5c, 5c .
    for moeda in Listamoeda:
        if moeda[-1] == "e":
            print(moeda[:-1])
        elif moeda[-1] == "c":
            print(moeda[:-1])
        elif moeda[-1] == ".":
            print(moeda[:-1])
        else:
            print("Moeda inválida")




def analisadorMoeda(Listamoeda):
    tokens = {
        "euros",
        "centimos",
        "ponto"
    }

    #t_ignore = ' \t\n'
    t_ponto = r'\.'

    
    def t_error(t):
        print(f"Carácter ilegal {t.value[0]}")
        t.lexer.skip(1)

    
    def t_euros(t):
        r'\d+e'
        t.value = int(t.value[:-1])
        print(t.value)
        return t
    
    def t_centimos(t):
        r'\d+c'
        t.value = int(t.value[:-1])
        print(t.value)
        return t
    
    lexer = lex.lex()
    ListamoedaString = " ".join(Listamoeda)
    print(ListamoedaString)
    lexer.input(ListamoedaString)
    while tok := lexer.token():
        print(tok)

