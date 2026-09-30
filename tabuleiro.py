import os
import time

import computador
import estatisticas
import jogador
import navios
import replay
import utils


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_tabuleiro(tabuleiro_atual, esconder_navios=False):
    print("      A B C D E F G H I J")
    print("    +---------------------+")

    for linha in range(10):
        print(f" {linha + 1:2} |", end=" ")

        for coluna in range(10):
            valor = tabuleiro_atual[linha][coluna]

            if esconder_navios and valor == "N":
                valor = "~"

            print(valor, end=" ")

        print("|")

    print("    +---------------------+")


def mostrar_status(jogador_atual):
    print(f"\nCOMANDANTE: {jogador_atual['nome']}")
    print(f"Acertos: {jogador_atual['acertos']}")
    print(f"Jogadas: {len(jogador_atual['jogadas'])}")


def mostrar_conferencia(jogador_atual):
    limpar_tela()

    print("==============================================")
    print("          CONFERÊNCIA DOS NAVIOS")
    print("==============================================")

    mostrar_tabuleiro(jogador_atual["tabuleiro"])

    print("\nNAVIOS:")

    for navio in jogador_atual["navios"]:
        posicoes = []

        for linha, coluna in navio["posicoes"]:
            posicoes.append(
                utils.coordenada_texto(linha, coluna)
            )

        print(
            f"- {navio['nome']}: "
            f"{', '.join(posicoes)}"
        )

    input("\nPressione ENTER para iniciar...")


def pedir_coordenada(jogador_atacante):
    while True:
        coordenada = input(
            f"\n{jogador_atacante['nome']} - "
            "Digite uma coordenada: "
        ).strip().upper()

        if not utils.coordenada_valida(coordenada):
            print(
                "Coordenada inválida. "
                "Use algo como C5 ou J10."
            )
            continue

        linha, coluna = utils.converter_coordenada(
            coordenada
        )

        if (linha, coluna) in jogador_atacante["jogadas"]:
            print(
                "Essa posição já foi utilizada. "
                "A rodada não será consumida."
            )
            continue

        return linha, coluna, coordenada


def realizar_jogada(jogador_atacante, jogador_defensor):
    linha, coluna, coordenada = pedir_coordenada(
        jogador_atacante
    )

    jogador_atacante["jogadas"].append(
        (linha, coluna)
    )

    valor = jogador_defensor["tabuleiro"][linha][coluna]

    if valor == "~":
        jogador_defensor["tabuleiro"][linha][coluna] = "O"

        print(f"\n{coordenada}: ÁGUA!")
        return "água", coordenada

    if valor == "N":
        jogador_defensor["tabuleiro"][linha][coluna] = "X"
        jogador_atacante["acertos"] += 1

        navio = navios.encontrar_navio(
            jogador_defensor["navios"],
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
                f"\n{coordenada}: ACERTO! "
                f"O navio {navio['nome']} foi afundado!"
            )
            return "afundado", coordenada

        print(f"\n{coordenada}: ACERTO!")
        return "acerto", coordenada

    return "erro", coordenada


def iniciar_partida(modo):
    jogador1 = jogador.criar_jogador("Jogador 1")

    if modo == 1:
        jogador2 = jogador.criar_jogador("Computador")
    else:
        jogador2 = jogador.criar_jogador("Jogador 2")

    mostrar_conferencia(jogador1)

    if modo == 2:
        mostrar_conferencia(jogador2)

    inicio = time.time()
    historico = []
    jogador_atual = jogador1
    adversario = jogador2

    while True:
        limpar_tela()

        print("==============================================")
        print("                 BATALHA NAVAL")
        print("==============================================")

        mostrar_status(jogador_atual)

        print("\nSEU TABULEIRO:")
        mostrar_tabuleiro(
            jogador_atual["tabuleiro"]
        )

        print("\nTABULEIRO INIMIGO:")
        mostrar_tabuleiro(
            adversario["tabuleiro"],
            esconder_navios=True
        )

        if jogador_atual["nome"] == "Computador":
            resultado, coordenada = computador.jogar(
                jogador_atual,
                adversario
            )
        else:
            resultado, coordenada = realizar_jogada(
                jogador_atual,
                adversario
            )

        historico.append(
            {
                "jogador": jogador_atual["nome"],
                "coordenada": coordenada,
                "resultado": resultado
            }
        )

        if navios.todos_afundados(adversario["navios"]):
            tempo = time.time() - inicio

            finalizar_partida(
                jogador_atual,
                adversario,
                historico,
                tempo
            )

            return

        input("\nPressione ENTER para continuar...")

        jogador_atual, adversario = (
            adversario,
            jogador_atual
        )


def finalizar_partida(
    vencedor,
    perdedor,
    historico,
    tempo
):
    limpar_tela()

    print("==============================================")
    print("                 FIM DE JOGO")
    print("==============================================")

    print(f"\nVENCEDOR: {vencedor['nome']}")
    print(f"Jogadas: {len(historico)}")
    print(f"Acertos: {vencedor['acertos']}")
    print(f"Tempo total: {tempo:.2f} segundos")

    replay.salvar_replay(
        historico,
        vencedor["nome"],
        tempo
    )

    estatisticas.registrar_partida(
        vencedor,
        perdedor
    )

    input("\nPressione ENTER para voltar ao menu...")
