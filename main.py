import shutil, os, pygame, keyboard
import assets

from colorama import init, Style, Fore, Back

largura = shutil.get_terminal_size().columns
init(autoreset=True)

while True:
    print("\033[H", end="")

    for linha in assets.titulo.splitlines():
        print(Fore.CYAN + linha.center(largura))

    tecla = keyboard.read_key()

    if tecla == 'down':
        for linha in assets.iniciar.splitlines():
            print(linha.center(largura))

        for linha in assets.sair.splitlines():
            print(Fore.RED + linha.center(largura))
    elif tecla == 'up':
        for linha in assets.iniciar.splitlines():
            print(Fore.RED + linha.center(largura))
    
        for linha in assets.sair.splitlines():
            print(linha.center(largura))