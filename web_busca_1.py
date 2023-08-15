from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# ABRINDO O NAVEGADOR
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com.br/')
time.sleep(1)

# DIGITANDO NO CAMPO DE BUSCA E CLICANDO EM BUSCAR
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('metal gear 3 remake')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()