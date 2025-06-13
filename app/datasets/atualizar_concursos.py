import requests
import os
from datetime import datetime

def baixar_csv():
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados/download?modalidade=LOTOFACIL"
    caminho = os.path.join("app", "datasets", "concursos_lotofacil.csv")

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200 and response.content.strip():
        with open(caminho, "wb") as f:
            f.write(response.content)
        print(f"✅ CSV atualizado com sucesso às {datetime.now().strftime('%H:%M:%S')}")
    else:
        print(f"❌ Erro ao baixar CSV. Status: {response.status_code}")

if __name__ == "__main__":
    baixar_csv()
