from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time
import traceback

def configurar_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 🔹 Último resultado oficial
def scrapear_resultado_lotofacil():
    try:
        url = "https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx"
        driver = configurar_driver()
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        raw_concurso = soup.select_one("#resultados .title-bar h2 span")
        match = re.search(r"\d{4,}", raw_concurso.get_text()) if raw_concurso else None
        concurso = int(match.group(0)) if match else None

        raw_data = soup.select_one(".section-text h2 > span")
        data = raw_data.get_text(strip=True) if raw_data else None

        dezenas_elements = soup.select("ul.simple-container.lista-dezenas.lotofacil li.dezena")
        dezenas = [li.get_text(strip=True).zfill(2) for li in dezenas_elements if li.get_text(strip=True).isdigit()]

        driver.quit()

        if not concurso or not data or len(dezenas) != 15:
            return None

        return {
            "concurso": concurso,
            "data_concurso": data,
            "dezenas_sorteadas": dezenas
        }

    except Exception as e:
        print("❌ Erro no scraping ao vivo:")
        traceback.print_exc()
        return None

# 🔹 Por número de concurso
def scrapear_resultado_por_numero(concurso_numero: int):
    try:
        url = "https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx"
        driver = configurar_driver()
        driver.get(url)
        time.sleep(3)

        input_element = driver.find_element("id", "ctl00_ContentPlaceHolder1_concResultado")
        input_element.clear()
        input_element.send_keys(str(concurso_numero))

        botao = driver.find_element("id", "ctl00_ContentPlaceHolder1_btnConsultar")
        botao.click()
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        raw_concurso = soup.select_one("div.title-bar.clearfix h2 span")
        match = re.search(r"\d{4,}", raw_concurso.get_text())
        concurso = int(match.group(0)) if match else None

        raw_data = soup.find("span", id="ctl00_ContentPlaceHolder1_lblData")
        data = raw_data.get_text(strip=True) if raw_data else None

        dezenas_elements = soup.select("ul#ulDezenasResultado li")
        dezenas = [li.get_text(strip=True).zfill(2)
                   for li in dezenas_elements if li.get_text(strip=True).isdigit()]

        driver.quit()

        if not concurso or not data or len(dezenas) != 15:
            return None

        return {
            "concurso": concurso,
            "data_concurso": data,
            "dezenas_sorteadas": dezenas
        }

    except Exception as e:
        print(f"❌ Erro ao buscar concurso {concurso_numero}:")
        traceback.print_exc()
        return None
