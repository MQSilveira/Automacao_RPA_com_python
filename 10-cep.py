
# EXEMPLO 01
# IDEAL PARA "MOSTRAR NA TELA"

from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui as tempo
import pyautogui as teclado


# Função para validar CEP
def valida_cep():
    
    while True:
        
        # Input do CEP
        cep = str(input('Digite o CEP: ')).strip()
        
        # Validação INT
        try:
            cep = int(cep)
            break
        
        except:
            pass
        
    return cep


# Dicionário que irá conter o endereço completo
endereco = dict()

cep = valida_cep()

# Navegador
chrome = webdriver.Chrome()

# Site que vou manipular
chrome.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

tempo.sleep(3)

# Irá acessar o elemento pelo ID 'endereco' (campo de pesquisa)
# .send_keys() - Irá digitar no elemento
chrome.find_element(By.ID, 'endereco').send_keys(cep)

tempo.sleep(1)

# Pressiona ENTER
teclado.press('enter')

# Tempo de espera após executar (5 segundos)
tempo.sleep(5)

try:
    # Logradouro/Nome
    endereco['Logradouro/Nome'] = chrome.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text

    # Bairro/Distrito.text
    endereco['Bairro/Distrito'] = chrome.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text

    # Localidade/UF.text
    endereco['Localidade/UF'] = chrome.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

    # CEP 
    endereco['CEP'] = chrome.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text


    for chave, valor in endereco.items():
        
        print(f'{chave}: {valor}')

except:
    print(f'\n{cep} não encontrado!')



# EXEMPLO 02 
# IDEAL PARA TRATAMENTO DE DADOS
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui as tempo
import pyautogui as teclado


# Função para validar CEP
def valida_cep():
    
    while True:
        
        # Input do CEP
        cep = str(input('Digite o CEP: ')).strip()
        
        # Validação INT
        try:
            cep = int(cep)
            break
        
        except:
            pass
    return cep


# Variável que irá conter o endereço completo
endereco = ''

cep = valida_cep()

# Navegador
chrome = webdriver.Chrome()

# Site que vou manipular
chrome.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

tempo.sleep(3)

# Irá acessar o elemento pelo ID 'endereco' (campo de pesquisa)
# .send_keys() - Irá digitar no elemento
chrome.find_element(By.ID, 'endereco').send_keys(cep)

tempo.sleep(1)

# Pressiona ENTER
teclado.press('enter')

# Tempo de espera após executar (5 segundos)
tempo.sleep(5)


# Variável tabela recebe elementoS (find_elements)
# Pesquisamos por xpath (XPATH), '//*[@id="resultado-DNEC"]' 
# Referente a tabela onde irá aparecer o resultado
tabela = chrome.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

# Loop para percorrer as linhas (tr) da tabela
for linha in tabela.find_elements(By.TAG_NAME, 'tr'):

    # Loop para percorrer as colunas (td) da linha
    for coluna in linha.find_elements(By.TAG_NAME, 'td'):
        
        # Concatenação das colunas para formar o endereço completo
        endereco += coluna.text + ';'


if endereco:
    # Print do endereço
    print(f'Endereço: {endereco}')
    
else:
    print(f'\n{cep} não encontrado!')
"""
