from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

def download_file():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : os.path.abspath("downloads")}
    options.add_experimental_option("prefs", prefs)
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
        time.sleep(3)
        download_button = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a")
        download_button.click()
        print("Arquivo baixado com sucesso.")
        time.sleep(5)
    finally:
        driver.quit()
