import requests
import pandas as pd
import os

def baixar_concursos():
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=LOTOFACIL"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        concursos = []
        for item in dados.get("listaResultado", []):
            dezenas = item.get("listaDezenas", [])
            if len(dezenas) == 15:
                concursos.append({
                    "Concurso": item.get("numero"),
                    "Data Sorteio": item.get("dataApuracao"),
                    **{f"Bola{i+1}": dezenas[i] for i in range(15)}
                })

        df = pd.DataFrame(concursos)
        path = os.path.join("app", "datasets", "concursos_lotofacil.csv")
        df.to_csv(path, index=False, sep=";", encoding="utf-8-sig")
        print("✅ CSV da Lotofácil salvo com sucesso!")
    else:
        print(f"❌ Erro ao baixar CSV. Status: {response.status_code}")

if __name__ == "__main__":
    baixar_concursos()
