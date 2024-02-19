


def parsingficheiro():
    dados = {}
    with open('emd.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(',')
            key = data[1]
            values = data
            dados[key] = values
    return dados

def listarModalidade(dados):
    modalidades = set()
    for linha in dados.values():
        modalidades.add(linha[8])
    return sorted(modalidades)



def main():
    dados = parsingficheiro()
    modalidades = listarModalidade(dados)

    print(f'Hi, {modalidades}')

if __name__ == '__main__':
    main()

