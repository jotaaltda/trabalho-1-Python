import json
import os


ARQUIVO = "data/estatisticas.json"


def criar_arquivo():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(ARQUIVO):
        dados = {
            "partidas": 0,
            "acertos": 0,
            "jogadas": 0
        }

        with open(
            ARQUIVO,
            "w",
            encoding="utf-8"
        ) as arquivo:
            json.dump(
                dados,
                arquivo,
                indent=4,
                ensure_ascii=False
            )


def carregar():
    criar_arquivo()

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:
        return json.load(arquivo)


def registrar_partida(vencedor, perdedor):
    dados = carregar()

    dados["partidas"] += 1
    dados["acertos"] += (
        vencedor["acertos"]
        + perdedor["acertos"]
    )
    dados["jogadas"] += (
        len(vencedor["jogadas"])
        + len(perdedor["jogadas"])
    )

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


def mostrar_estatisticas():
    dados = carregar()

    print("\n==============================================")
    print("                 ESTATÍSTICAS")
    print("==============================================")

    print(f"\nPartidas: {dados['partidas']}")
    print(f"Acertos: {dados['acertos']}")
    print(f"Jogadas: {dados['jogadas']}")

    if dados["jogadas"] > 0:
        aproveitamento = (
            dados["acertos"]
            / dados["jogadas"]
            * 100
        )
    else:
        aproveitamento = 0

    print(
        f"Aproveitamento: {aproveitamento:.2f}%"
    )
