import navios


def criar_tabuleiro():
    tabuleiro = []

    for _ in range(10):
        linha = []

        for _ in range(10):
            linha.append("~")

        tabuleiro.append(linha)

    return tabuleiro


def criar_jogador(nome):
    jogador = {
        "nome": nome,
        "tabuleiro": criar_tabuleiro(),
        "navios": navios.criar_navios(),
        "jogadas": [],
        "acertos": 0
    }

    navios.posicionar_todos(
        jogador["tabuleiro"],
        jogador["navios"]
    )

    return jogador
