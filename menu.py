import os
import shutil
import time

import keyboard
from colorama import Fore, Style, init

import estatisticas
import replay
import tabuleiro


init(autoreset=True)

LARGURA = shutil.get_terminal_size().columns


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def centralizar(texto):
    for linha in texto.splitlines():
        print(linha.center(LARGURA))


def titulo():
    print(Fore.CYAN + Style.BRIGHT)
    centralizar("╔══════════════════════════════════════════════════════╗")
    centralizar("║                      BATALHA NAVAL                   ║")
    centralizar("╚══════════════════════════════════════════════════════╝")
    print(Style.RESET_ALL)


def mostrar_menu(opcao):
    limpar_tela()
    titulo()

    print()
    centralizar(Fore.WHITE + "╭────────────────────────────────────────────────────╮")
    centralizar(Fore.WHITE + "│                  CENTRAL DE COMANDO                │")
    centralizar(Fore.WHITE + "╰────────────────────────────────────────────────────╯")
    print()

    opcoes = [
        "NOVA PARTIDA",
        "ESTATÍSTICAS",
        "REPLAY",
        "COMO JOGAR",
        "SAIR"
    ]

    for i, texto in enumerate(opcoes):
        if i == opcao:
            prefixo = Fore.CYAN + Style.BRIGHT + "  >>> "
            texto_cor = Fore.CYAN + Style.BRIGHT + texto
            sufixo = Fore.CYAN + Style.BRIGHT + " <<<"
        else:
            prefixo = Fore.WHITE + "      "
            texto_cor = Fore.WHITE + texto
            sufixo = ""

        print((prefixo + texto_cor + sufixo).center(LARGURA))

    print()
    centralizar(
        Fore.LIGHTBLACK_EX
        + "↑ ↓  navegar     ENTER  selecionar     Q  sair"
    )


def menu_partida():
    opcao = 0

    while True:
        limpar_tela()
        titulo()

        print()
        centralizar("╔══════════════════════════════════════════════════════╗")
        centralizar("║                    NOVA PARTIDA                    ║")
        centralizar("╚══════════════════════════════════════════════════════╝")
        print()

        opcoes = [
            "JOGADOR  x  COMPUTADOR",
            "JOGADOR  x  JOGADOR",
            "VOLTAR"
        ]

        for i, texto in enumerate(opcoes):
            if i == opcao:
                print(
                    (
                        Fore.YELLOW
                        + Style.BRIGHT
                        + f"  >>> {texto} <<<"
                    ).center(LARGURA)
                )
            else:
                print(
                    (Fore.WHITE + f"      {texto}").center(LARGURA)
                )

        print()
        centralizar(
            Fore.LIGHTBLACK_EX
            + "↑ ↓  navegar     ENTER  selecionar"
        )

        tecla = keyboard.read_key().lower()

        if tecla == "down":
            opcao = (opcao + 1) % len(opcoes)

        elif tecla == "up":
            opcao = (opcao - 1) % len(opcoes)

        elif tecla in ("enter", "z"):
            if opcao == 0:
                tabuleiro.iniciar_partida(1)
            elif opcao == 1:
                tabuleiro.iniciar_partida(2)
            else:
                return


def mostrar_como_jogar():
    limpar_tela()
    titulo()

    print()
    centralizar("╔══════════════════════════════════════════════════════╗")
    centralizar("║                    COMO JOGAR                      ║")
    centralizar("╚══════════════════════════════════════════════════════╝")
    print()

    regras = [
        "O tabuleiro possui 10 x 10 posições.",
        "As colunas vão de A até J e as linhas de 1 até 10.",
        "Cada jogador possui um navio pequeno e um grande.",
        "O pequeno ocupa 2 posições.",
        "O grande ocupa 4 posições.",
        "Os navios são posicionados automaticamente.",
        "Informe as coordenadas no formato C5, A10, J2 etc.",
        "O = água    X = acerto    N = navio",
        "Vence quem afundar todos os navios adversários."
    ]

    for regra in regras:
        centralizar(Fore.WHITE + "• " + regra)

    print()
    centralizar(Fore.CYAN + "Boa caçada, comandante.")
    input("\nPressione ENTER para voltar...")


def menu():
    opcao = 0

    while True:
        mostrar_menu(opcao)

        tecla = keyboard.read_key().lower()

        if tecla == "down":
            opcao = (opcao + 1) % 5

        elif tecla == "up":
            opcao = (opcao - 1) % 5

        elif tecla in ("enter", "z"):
            if opcao == 0:
                menu_partida()
            elif opcao == 1:
                estatisticas.mostrar_estatisticas()
                input("\nPressione ENTER para voltar...")
            elif opcao == 2:
                replay.executar_replay()
            elif opcao == 3:
                mostrar_como_jogar()
            elif opcao == 4:
                limpar_tela()
                centralizar(Fore.CYAN + "Encerrando sistema...")
                time.sleep(0.5)
                return

        elif tecla == "q":
            limpar_tela()
            return