import shutil, os, pygame, keyboard
import assets, funcoes

from colorama import init, Style, Fore, Back

largura = shutil.get_terminal_size().columns
init(autoreset=True)

pygame.init()
pygame.mixer.init()

while True:
    print("\033[H", end="")

    for linha in assets.titulo.splitlines():
        print(Fore.CYAN + linha.center(largura))
    for linha in assets.iniciar.splitlines():
        print(Fore.RED + linha.center(largura))
    for linha in assets.sair.splitlines():
        print(linha.center(largura))
    opcao = 2

    tecla = keyboard.read_key()

    if tecla == 'down':
        print("\033[H", end="")
        for linha in assets.titulo.splitlines():
            print(Fore.CYAN + linha.center(largura))
        for linha in assets.iniciar.splitlines():
            print(linha.center(largura))
        for linha in assets.sair.splitlines():
            print(Fore.RED + linha.center(largura))
        opcao = 1
    elif tecla == 'up':
        print("\033[H", end="")
        for linha in assets.titulo.splitlines():
            print(Fore.CYAN + linha.center(largura))
        for linha in assets.iniciar.splitlines():
            print(Fore.RED + linha.center(largura))
        for linha in assets.sair.splitlines():
            print(linha.center(largura))
        opcao = 2

    confirma = keyboard.read_key()

    if opcao == 1 and confirma == 'z':
        os.system('cls')
        exit(0)