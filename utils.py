import os
import re

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def esperar():
    input("\nPressione ENTER para continuar...")

def coordenada_valida(coordenada):
    if not re.fullmatch(r"[A-Ja-j](10|[1-9])", coordenada):
        return False

    return True

def converter_coordenada(coordenada):
    coordenada = coordenada.upper()

    coluna = ord(coordenada[0]) - ord("A")
    linha = int(coordenada[1:]) - 1

    return linha, coluna

def coordenada_texto(linha, coluna):
    letra = chr(ord("A") + coluna)

    return f"{letra}{linha + 1}"