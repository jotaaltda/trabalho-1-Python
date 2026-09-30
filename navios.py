import random

def criar_navios():
    navios = [
        {
            'Nome': 'Pequeno',
            'Tamanho': 2,
            'Posicoes': [],
            'Atingidas': []
        },

        {
            'Nome': 'Pequeno',
            'Tamanho': 2,
            'Posicoes': [],
            'Atingidas': []
        }
    ]

    return navios

def gerar_posicoes(linha, coluna, tamanho, horizontal):
    posicoes = []

    for i in range(tamanho):
        if horizontal:
            nova_linha = linha
            nova_coluna = coluna + i
        else:
            nova_linha = linha + i
            nova_coluna = coluna

    posicoes.append((nova_linha, nova_coluna))

    return posicoes

def posicoes_validas(posicoes, tabuleiro):
    for linha, coluna in posicoes:
        if linha < 0 or linha >= 10:
            return False
        if coluna < 0 or coluna >= 10:
            return False
        if tabuleiro[linha][coluna] != "~":
            return False

    return True