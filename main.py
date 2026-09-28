import shutil, os, pygame, keyboard
import assets

from colorama import init, Style, Fore, Back

largura = shutil.get_terminal_size().columns
init(autoreset=True)

for linha in assets.titulo.splitlines():
    print(linha.center(largura))