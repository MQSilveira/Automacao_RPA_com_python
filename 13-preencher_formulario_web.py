from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pyautogui as tempo
import pyautogui as teclado


# Navegador
chrome = webdriver.Chrome()

# Site que vou manipular (formulário)
chrome.get('https://www.jotform.com/221436066464051')

# Tempo de espera após executar (3 segundos)
tempo.sleep(3)


# Nome
chrome.find_element(By.NAME, 'q3_nome[first]').send_keys('Marcos')
tempo.sleep(1)


# Sobrenome
chrome.find_element(By.NAME, 'q3_nome[last]').send_keys('Silveira')
tempo.sleep(1)


# E-mail
chrome.find_element(By.NAME, 'q4_email').send_keys('emaildomarcos@gmail.com')
tempo.sleep(1)


# Rola a tela apertando Page Down
teclado.keyDown('PgDn')


# Estado Civil
# Variável recebendo o DropDown de Estado Civil
drop_down = chrome.find_element(By.ID, 'input_5')

# Váriável recebendo as opções disponíveis de drop_down
item_drop_down = Select(drop_down)

# Escolho a opção desejada
# item_drop_down.select_by_value('Casado(a)')       # Precisa está exatamente igual
# item_drop_down.select_by_visible_text('Casado')   # Por texto visivel

item_drop_down.select_by_index(2)
"""
0 - Please Select
1 - Solteiro(a)
2 - Casado(a)
3 - Divorciado(a)
4 - Viuvo(a)
"""
tempo.sleep(1)


# Tem Filhos
# Variável confirmando se possui (True) filhos ou não (False)
filhos = False

# Validação
if filhos:
    chrome.find_element(By.ID, 'label_input_6_0').click()
else:
    chrome.find_element(By.ID, 'label_input_6_1').click()

tempo.sleep(1)


# Cores Favoritas
"""
Azul        ID - label_input_7_0
Amarelo     ID - label_input_7_1
Vermelho    ID - label_input_7_2
Laranja     ID - label_input_7_3
Preto       ID - label_input_7_4
Verde       ID - label_input_7_5
"""
# Azul
chrome.find_element(By.ID, 'label_input_7_0').click()

# Laranja
chrome.find_element(By.ID, 'label_input_7_3').click()

# Verde
chrome.find_element(By.ID, 'label_input_7_5').click()
tempo.sleep(1)


# Rola a tela apertando Page Down
teclado.keyDown('PgDn')


# Avaliação
"""
1 Estrela - //*[@id="input_8"]/div[1]
2 Estrela - //*[@id="input_8"]/div[2]
3 Estrela - //*[@id="input_8"]/div[3]
4 Estrela - //*[@id="input_8"]/div[4]
5 Estrela - //*[@id="input_8"]/div[5]
"""

# 5 Estrelas
chrome.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()
tempo.sleep(1)


# Insira uma pergunta aqui
"""
Qualidade do Serviço
Insatisfeito(a) -       input_9_0_0
Pouco Satisfeito(a) -   input_9_0_1
Satisfeito(a) -         input_9_0_2
Muito Satisfeito(a) -   input_9_0_3

Grau de Dificuldade
Insatisfeito(a) -       input_9_1_0
Pouco Satisfeito(a) -   input_9_1_1
Satisfeito(a) -         input_9_1_2
Muito Satisfeito(a) -   input_9_1_3
"""
# Qualidade do Serviço - Muito Satisfeito(a)
chrome.find_element(By.ID, 'input_9_0_3').click()

# Grau de Dificuldade - Muito Satisfeito(a)
chrome.find_element(By.ID, 'input_9_1_3').click()
tempo.sleep(1)


# Enviar 
tempo.sleep(1)
#chrome.find_element(By.ID, 'input_2').click()

print('Fim do Formulário')

