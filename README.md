# Batalha Naval

Projeto individual de Batalha Naval desenvolvido em Python.

## Estrutura

```text
BatalhaNaval/
├── main.py
├── menu.py
├── tabuleiro.py
├── navios.py
├── jogador.py
├── computador.py
├── estatisticas.py
├── replay.py
├── utils.py
├── data/
├── docs/
└── README.md
```

## Requisitos

- Python 3.10 ou superior
- colorama
- keyboard

Instalação:

```bash
python -m pip install colorama keyboard
```

No Windows:

```bash
py -3.11 -m pip install colorama keyboard
```

## Execução

```bash
python main.py
```

No Windows:

```bash
py -3.11 main.py
```

## Modos

- Jogador x Computador
- Jogador x Jogador

## Regras

O tabuleiro possui 10 x 10 posições.

As coordenadas utilizam letras de A a J e números de 1 a 10.

Cada jogador possui:
- 1 navio pequeno de 2 posições
- 1 navio grande de 4 posições

Os navios são posicionados automaticamente e não podem ocupar a mesma posição.

Uma jogada repetida é rejeitada sem consumir a rodada.

Um navio é afundado quando todas as suas posições são atingidas.

A partida termina quando todos os navios de um jogador são afundados.

## Símbolos

- `~` = água / posição desconhecida
- `N` = navio
- `O` = tiro na água
- `X` = posição atingida

## Funcionalidades extras

- Histórico da partida
- Estatísticas
- Aproveitamento
- Replay da última partida
- Conferência dos navios antes da partida
- Tempo total de jogo
