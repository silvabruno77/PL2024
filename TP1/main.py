


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

def percentagemAptos(dados):
    total_atletas = len(dados)
    print(total_atletas)
    aptos = 0
    nao_aptos = 0
    for atleta in dados.values():
        if atleta[12] == "true":
            aptos += 1
        else:
            nao_aptos += 1
    print(aptos)
    print(nao_aptos)
    porcentagem_aptos = (aptos / total_atletas) * 100
    porcentagem_nao_aptos = (nao_aptos / total_atletas) * 100
    print(distribuicaoAtletas(dados))

    return porcentagem_aptos, porcentagem_nao_aptos

def distribuicaoAtletas(dados):
    escaloes = {}
    for atleta in dados.values():
        idade = int(atleta[5])
        escalao = idade // 5
        escalao = f'{escalao * 5} - {escalao * 5 + 4}'
        if escalao in escaloes:
            escaloes[escalao] += 1
        else:
            escaloes[escalao] = 1
    return escaloes

def main():
    dados = parsingficheiro()
    print(dados)
    modalidades = listarModalidade(dados)

    print(f'Modalidades, {modalidades}')

    porcentagem_aptos,porcentagem_nao_aptos = percentagemAptos(dados)

    print(f'Porcentagem Aptos:{porcentagem_aptos} Porcentagem Nao Aptos: {porcentagem_nao_aptos}')




if __name__ == '__main__':
    main()

