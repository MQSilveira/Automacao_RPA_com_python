from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui as tempo
import pyautogui as teclado

import pandas


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
    lista = list()
    
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
            
            lista.append(endereco)

        except:
            lista.append(f'{valor} NÃO encontrado!')
            
            
        # Nova Busca
        chrome.find_element(By.XPATH, '//*[@id="btn_nbusca"]').click()
        
        # Tempo de espera após executar (5 segundos)
        tempo.sleep(5)
        
        
    # Executa a função que exporta para o Excel
    # Nesse caso, não iriamos precisar do RETURN
    add_excel(lista)
        
        
    # Retorna uma lista contendo as informações dos CEPs
    # return lista
        

# Função para exportar CEPs para o Excel
def add_excel(lista_dict):
    
    # Lista utilizada para testes
    """
    lista_dict = [{'Logradouro/Nome': 'Rua Paulo Zimmermann	', 'Bairro/Distrito': 'Centro', 'Localidade/UF': 'Blumenau/SC', 'CEP': '89010-170'},
         {'Logradouro/Nome': 'Rua República Argentina - até 841 - lado ímpar', 'Bairro/Distrito': 'Ponta Aguda	', 'Localidade/UF':'Blumenau/SC	', 'CEP': '89050-101'},
         '9646544654654 NÃO encontrado!']
    """
    
    # Lista que irá conter os endereços
    lista = list()
    
    for item in lista_dict:
        
        # Variável temporária utilizada na conversão dict/list
        endereco = ''
        
        # Validação de dicionário
        if type(item) == dict:
            
            endereco += item['Logradouro/Nome'] + ';' + item['Bairro/Distrito'] + ';' + item['Localidade/UF'] + ';' + item['CEP']
            lista.append(endereco)
        
        else:
            # Se item não for um dict (significa quem o CEP não foi encontrado)
            # Irá salvar a mensagem informando a situação
            lista.append(item)
        
    # Preparo o arquivo excel usando o XLSXWRITER
    # dados_site será o nome do arquivo Excel
    # engine='xlsxwriter' - xlsxwriter é a biblioteca que quero usar
    arqExcel = pandas.ExcelWriter('enderecos.xlsx', engine='xlsxwriter')
            
  
    #DATAFRAME recebe pandas.DataFrame
    # Passando a lista com as linhas
    # columns irá receber o NOME da COLUNA do arquivo EXCEL
    dataFrame = pandas.DataFrame(lista, columns=['Logradouro/Nome;Bairro/Distrito;Localidade/UF;CEP'])

    # Na variável dataFrame, vou passar o arquivo EXCEL que preparamos
    # sheet_name é o nome da planilha
    # index = True, significa que estou autorizando a colocar o 
    # index (linhas na tabela) (0, 1, 2, 3...)
    dataFrame.to_excel(arqExcel, sheet_name='Planilha_CEPs', index=True)

    # Salva o arquivo Excel
    arqExcel.save()
    
    
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

# Lista utilizada para testes
"""
lista = [{'Logradouro/Nome': 'Rua Paulo Zimmermann	', 'Bairro/Distrito': 'Centro', 'Localidade/UF': 'Blumenau/SC', 'CEP': '89010-170'},
         {'Logradouro/Nome': 'Rua República Argentina - até 841 - lado ímpar', 'Bairro/Distrito': 'Ponta Aguda	', 'Localidade/UF':'Blumenau/SC	', 'CEP': '89050-101'}, 
         '9646544654654 NÃO encontrado!']
"""

#add_excel(lista)

