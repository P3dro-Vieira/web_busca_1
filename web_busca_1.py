from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# ABRINDO O NAVEGADOR
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com/')
time.sleep(1)

# DIGITANDO NO CAMPO DE BUSCA E CLICANDO EM BUSCAR
driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input').send_keys('metal gear 3 remake')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input').send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string').click()
time.sleep(85)
driver.quit() 