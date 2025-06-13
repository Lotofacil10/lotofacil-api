import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scraper_resultado_lotofacil():
    url = "https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        concurso_raw = soup.find(id="ctl00_ContentPlaceHolder1_lblConcurso")
        dezenas_raw = soup.find_all("span", class_="numero-sorteio")

        if not concurso_raw or not dezenas_raw:
            raise ValueError("Conteúdo esperado não encontrado na página.")

        concurso = int(concurso_raw.get_text(strip=True).split(" ")[-1])
        dezenas = [d.get_text(strip=True) for d in dezenas_raw]

        data = datetime.today().strftime("%d/%m/%Y")

        return {
            "concurso": concurso,
            "data_concurso": data,
            "dezenas_sorteadas": dezenas
        }

    except Exception as e:
        print(f"❌ Erro no scraping: {e}")
        raise
