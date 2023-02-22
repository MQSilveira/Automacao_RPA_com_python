from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui as tempo
import pyautogui as teclado


# Função para validar os CEPs
def valida_cep():
    
    # Lista que irá contar os CEPs
    ceps = list()
    
    # Contador
    n = 1
    while len(ceps) < 3:
        
        # Input do CEP
        cep = str(input(f'Digite o {n}º CEP: ')).strip()
        
        # Validação INT
        try:
            cep = int(cep)
            ceps.append(cep)
            n += 1
        
        except:
            pass
    return ceps


# Função para pesquisar CEP
def pesquisa_cep(ceps):
    
    # Lista que irá conter todos os dicionários com os endereços
    lista_temp = list()
    
    # Navegador
    chrome = webdriver.Chrome()

    # Site que vou manipular
    chrome.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

    tempo.sleep(3)

    # Loop para percorrer o indice de CEPs
    for indice, valor in enumerate(ceps):
        
        # Dicionário que irá conter o endereço completo
        # Dicionário é "zerado" a cada loop
        endereco = dict()
        
        # Irá acessar o elemento pelo ID 'endereco' (campo de pesquisa)
        # .send_keys() - Irá digitar no elemento
        chrome.find_element(By.ID, 'endereco').send_keys(valor)

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
            
            lista_temp.append(endereco)

        except:
            lista_temp.append(f'{valor} NÃO encontrado!')
            
            
        # Nova Busca
        chrome.find_element(By.XPATH, '//*[@id="btn_nbusca"]').click()
        
        # Tempo de espera após executar (5 segundos)
        tempo.sleep(5)


    # Retorna uma lista contendo as informaações dos CEPs
    return lista_temp
        

def mostrar_resultado(lista):
    
    for cep in lista:
        
        # Quebra linha
        print()
        
        # Se CEP for um dicionário:
        if type(cep) == dict:
            
            for chave, valor in cep.items():
                print(f'{chave}: {valor}')
                
        else:
            print(f'{cep}')
    

# Lista que irá contar os CEPs
ceps = list()
    
# Dicionário que irá conter o endereço completo
endereco = dict()

# Lista que irá conter todos os dicionários com os endereços
lista = list()

# Atribundo os CEPs validados na função
ceps = valida_cep()

# Chama a função pesquisa atribuindo a lista com CEPs
lista = pesquisa_cep(ceps)

print(lista)

"""
lista = [{'Logradouro/Nome': 'Rua Paulo Zimmermann	', 'Bairro/Distrito': 'Centro', 'Localidade/UF': 'Blumenau/SC', 'CEP': '89010-170'},
         {'Logradouro/Nome': 'Rua República Argentina - até 841 - lado ímpar', 'Bairro/Distrito': 'Ponta Aguda	', 'Localidade/UF':'Blumenau/SC	', 'CEP': '89050-101'}, 
         '9646544654654 NÃO encontrado!']

"""

# Chama a função mostrar_resultado atribuindo a lista com informações dos CEPs
# mostrar_resultado(lista)

mostrar_resultado(lista)

