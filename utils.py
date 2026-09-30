import re


def coordenada_valida(coordenada):
    if re.fullmatch(
        r"[A-Ja-j](10|[1-9])",
        coordenada
    ):
        return True

    return False


def converter_coordenada(coordenada):
    coordenada = coordenada.upper()

    coluna = ord(coordenada[0]) - ord("A")
    linha = int(coordenada[1:]) - 1

    return linha, coluna


def coordenada_texto(linha, coluna):
    letra = chr(ord("A") + coluna)

    return f"{letra}{linha + 1}"
