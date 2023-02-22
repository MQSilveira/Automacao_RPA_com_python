from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pyautogui


# Navegador
chrome = webdriver.Chrome()

# Site que vou manipular (formulário)
chrome.get('https://pt.surveymonkey.com/r/7GX9XRZ')

# Tempo de espera após executar (3 segundos)
pyautogui.sleep(3)


# Nome
chrome.find_element(By.ID, '72542598').send_keys('Marcos')
pyautogui.sleep(1)

# Email
chrome.find_element(By.ID, '72542821').send_keys('emaildomarcos@gmail.com')
pyautogui.sleep(1)


# Sexo
# Variável referente ao sexo (M masculino / F feminino)
sexo = 'M'

# Validação 
if sexo == 'M':
    chrome.find_element(By.XPATH, '//*[@id="72542994_583517054_label"]/span[2]').click()

else:
    chrome.find_element(By.XPATH, '//*[@id="72542994_583517055_label"]/span[2]')

pyautogui.sleep(1)

# Rola a tela apertando Page Down
pyautogui.keyDown('PgDn')


# Cor
# Variável recebendo o DropDown de cor
drop_down = chrome.find_element(By.ID, '72543178')

# Váriável recebendo as opções disponíveis de drop_down
item_drop_down = Select(drop_down)

# item_drop_down.select_by_visible_text('Azul')     # Por texto visivel

# Por indice
item_drop_down.select_by_index(1)
pyautogui.sleep(1)


# Concluido 
#chrome.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()


print('Fim do Formulário')


