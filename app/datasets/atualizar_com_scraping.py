import requests
from bs4 import BeautifulSoup

def fetch_last_results():
    url = "https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx"
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.content, "html.parser")
    table = soup.select_one("table.simple-table.results-table")
    rows = table.select("tr")[1:26]
    data = []
    for row in rows:
        cols = row.select("td")
        concurso = int(cols[0].get_text(strip=True))
        dezenas = [int(li.get_text()) for li in cols[1].select("li")]
        data.append({"concurso": concurso, "dezenas": dezenas})
    return data
