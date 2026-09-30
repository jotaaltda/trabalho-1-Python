import json
import os
import time


ARQUIVO = "data/replay.json"


def salvar_replay(historico, vencedor, tempo):
    if not os.path.exists("data"):
        os.makedirs("data")

    dados = {
        "vencedor": vencedor,
        "tempo": tempo,
        "jogadas": historico
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


def executar_replay():
    if not os.path.exists(ARQUIVO):
        print("\nNenhuma partida foi registrada ainda.")
        input("\nPressione ENTER para voltar...")
        return

    with open(
        ARQUIVO,
        "r",
        encoding="utf-8"
    ) as arquivo:
        dados = json.load(arquivo)

    print("\n==============================================")
    print("                    REPLAY")
    print("==============================================")

    print(f"\nVencedor: {dados['vencedor']}")
    print(f"Tempo: {dados['tempo']:.2f} segundos")
    print("\nJogadas:\n")

    for numero, jogada in enumerate(
        dados["jogadas"],
        start=1
    ):
        print(
            f"{numero:02} | "
            f"{jogada['jogador']} | "
            f"{jogada['coordenada']} | "
            f"{jogada['resultado']}"
        )

        time.sleep(0.35)

    input("\nPressione ENTER para voltar...")
