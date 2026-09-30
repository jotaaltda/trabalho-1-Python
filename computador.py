import random

import navios
import utils


def escolher_jogada(computador):
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if (linha, coluna) not in computador["jogadas"]:
            return linha, coluna


def jogar(computador, defensor):
    linha, coluna = escolher_jogada(computador)

    computador["jogadas"].append((linha, coluna))

    coordenada = utils.coordenada_texto(
        linha,
        coluna
    )

    valor = defensor["tabuleiro"][linha][coluna]

    if valor == "~":
        defensor["tabuleiro"][linha][coluna] = "O"

        print(
            f"\nComputador jogou {coordenada}: ÁGUA!"
        )

        return "água", coordenada

    defensor["tabuleiro"][linha][coluna] = "X"
    computador["acertos"] += 1

    navio = navios.encontrar_navio(
        defensor["navios"],
        linha,
        coluna
    )

    navios.acertar_navio(
        navio,
        linha,
        coluna
    )

    if navios.navio_afundado(navio):
        print(
            f"\nComputador jogou {coordenada}: "
            f"ACERTO! {navio['nome']} afundado!"
        )

        return "afundado", coordenada

    print(
        f"\nComputador jogou {coordenada}: ACERTO!"
    )

    return "acerto", coordenada
