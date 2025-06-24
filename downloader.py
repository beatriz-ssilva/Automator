from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

def download_file():
    #criar a pasta se não existir
    download_path = os.path.abspath("downloads")
    os.makedirs(download_path, exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_path}
    options.add_experimental_option("prefs", prefs)

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
        time.sleep(3)
        download_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Download sample pdf file')]")
        download_button.click()
        print("Arquivo sendo baixado...")
        time.sleep(5)  #verificar se o arquivo terminou o download
        print("Arquivo baixado com sucesso.")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
    finally:
        driver.quit()
