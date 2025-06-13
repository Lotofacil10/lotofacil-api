from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx")
time.sleep(3)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

print("\n🔍 Trecho do HTML capturado:")
print(soup.prettify()[:2000])  # Mostra os primeiros 2000 caracteres
