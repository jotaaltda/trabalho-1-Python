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

    for linha in matriz:
        print(" ".join(linha).center(largura))