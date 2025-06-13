import pandas as pd
import numpy as np
import joblib
import os

def dezenas_para_binario(dezenas):
    vetor = [0] * 25
    for dezena in dezenas:
        if 1 <= dezena <= 25:
            vetor[dezena - 1] = 1
    return vetor

def binario_para_dezenas(vetor_binario):
    return [i + 1 for i, bit in enumerate(vetor_binario) if bit == 1]

def gerar_jogos_ia(qtd=5):
    modelo_path = os.path.join("app", "models", "modelo_ia_lotofacil.pkl")
    csv_path = os.path.join("app", "datasets", "concursos_lotofacil.csv")

    if not os.path.exists(modelo_path):
        raise FileNotFoundError("❌ Modelo IA não encontrado.")
    if not os.path.exists(csv_path):
        raise FileNotFoundError("❌ CSV de concursos não encontrado.")

    modelo = joblib.load(modelo_path)
    df = pd.read_csv(csv_path, sep=";", encoding="latin1")
    col_dezenas = [col for col in df.columns if col.lower().startswith("bola")]
    ultima_linha = df.iloc[-1][col_dezenas].dropna().astype(int).tolist()

    if len(ultima_linha) < 15:
        raise ValueError("❌ Último concurso inválido.")

    entrada = np.array([dezenas_para_binario(ultima_linha)])
    jogos = []

    for _ in range(qtd):
        previsao = modelo.predict(entrada)[0]
        dezenas = binario_para_dezenas(previsao)
        if len(dezenas) > 15:
            dezenas = sorted(dezenas)[:15]
        elif len(dezenas) < 15:
            faltando = 15 - len(dezenas)
            restantes = [d for d in range(1, 26) if d not in dezenas]
            dezenas += np.random.choice(restantes, faltando, replace=False).tolist()

        jogos.append(sorted(dezenas))

    return jogos

if __name__ == "__main__":
    jogos = gerar_jogos_ia(5)
    for i, jogo in enumerate(jogos, 1):
        print(f"Jogo {i}: {jogo}")
