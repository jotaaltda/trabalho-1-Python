import shutil, os, pygame, keyboard
import assets, funcoes, menu

from colorama import init, Style, Fore, Back

largura = shutil.get_terminal_size().columns
init(autoreset=True)

def gerar_tabuleiro():
    matriz = [["⬜" for _ in range(11)] for _ in range(11)]

    for i in range(10):
        matriz[0][i + 1] = str(i)
    for i in range(10):
        matriz[i + 1][0] = chr(65 + i)

    titulo1 = "JOGADOR"
    titulo2 = "COMPUTADOR"

    distancia = " " * 10

    print((titulo1.center(21) + distancia + titulo2.center(21)).center(largura))

    for linha in matriz:
        esquerda = " ".join(linha)
        direita = " ".join(linha)

        print((esquerda + distancia + direita).center(largura))