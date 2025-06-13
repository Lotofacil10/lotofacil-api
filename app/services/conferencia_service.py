from typing import List


def conferir_jogo(dezenas_jogo: List[int], dezenas_sorteadas: List[int]) -> dict:
    acertos = list(set(dezenas_jogo) & set(dezenas_sorteadas))
    quantidade_acertos = len(acertos)

    return {
        "dezenas_jogo": sorted(dezenas_jogo),
        "dezenas_sorteadas": sorted(dezenas_sorteadas),
        "acertos": sorted(acertos),
        "quantidade_acertos": quantidade_acertos,
        "status": gerar_status(quantidade_acertos)
    }


def gerar_status(qtd: int) -> str:
    if qtd == 15:
        return "🏆 Parabéns, você acertou os 15 pontos!"
    elif qtd == 14:
        return "🎯 Acertou 14 pontos!"
    elif qtd == 13:
        return "👍 Acertou 13 pontos."
    elif qtd == 12:
        return "👌 Acertou 12 pontos."
    elif qtd == 11:
        return "✔️ Acertou 11 pontos."
    else:
        return "❌ Menos de 11 pontos."
