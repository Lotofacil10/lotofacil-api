import os
import requests
import pandas as pd
from app.models.treinar_modelo import treinar_modelo

def baixar_csv_oficial():
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=LOTOFACIL"
    destino = os.path.join("app", "datasets", "concursos_lotofacil.csv")

    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, "wb") as f:
            f.write(response.content)
        print("✅ CSV oficial atualizado com sucesso!")
    else:
        print(f"❌ Erro ao baixar CSV. Status: {response.status_code}")

if __name__ == "__main__":
    baixar_csv_oficial()
    treinar_modelo()
