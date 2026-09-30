import random


def criar_navios():
    return [
        {
            "nome": "Pequeno",
            "tamanho": 2,
            "posicoes": [],
            "atingidas": []
        },
        {
            "nome": "Grande",
            "tamanho": 4,
            "posicoes": [],
            "atingidas": []
        }
    ]


def gerar_posicoes(linha, coluna, tamanho, horizontal):
    posicoes = []

    for i in range(tamanho):
        if horizontal:
            posicoes.append((linha, coluna + i))
        else:
            posicoes.append((linha + i, coluna))

    return posicoes


def posicoes_validas(posicoes, tabuleiro):
    for linha, coluna in posicoes:
        if linha < 0 or linha >= 10:
            return False

        if coluna < 0 or coluna >= 10:
            return False

        if tabuleiro[linha][coluna] != "~":
            return False

    return True


def posicionar_navio(tabuleiro, navio):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        horizontal = random.choice([True, False])

        posicoes = gerar_posicoes(
            linha,
            coluna,
            navio["tamanho"],
            horizontal
        )

        if posicoes_validas(posicoes, tabuleiro):
            navio["posicoes"] = posicoes

            for linha_navio, coluna_navio in posicoes:
                tabuleiro[linha_navio][coluna_navio] = "N"

            return


def posicionar_todos(tabuleiro, lista_navios):
    for navio in lista_navios:
        posicionar_navio(tabuleiro, navio)


def encontrar_navio(lista_navios, linha, coluna):
    for navio in lista_navios:
        if (linha, coluna) in navio["posicoes"]:
            return navio

    return None


def acertar_navio(navio, linha, coluna):
    if (linha, coluna) not in navio["atingidas"]:
        navio["atingidas"].append((linha, coluna))


def navio_afundado(navio):
    return len(navio["atingidas"]) == navio["tamanho"]


def todos_afundados(lista_navios):
    for navio in lista_navios:
        if not navio_afundado(navio):
            return False

    return True
