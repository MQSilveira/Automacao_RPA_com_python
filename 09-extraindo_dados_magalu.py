from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui as tempo
import pyautogui as teclado

# tempo será utilizado para manipular o tempo de espera
# teclado será utilizado para manipular as teclas do teclado

import pandas

# Input recebendo o item a ser pesquisado no site
pesquisa = str(input('Digite o item a ser pesquisado: '))

# Navegador
chrome = webdriver.Chrome()

# Site que vou querer "manipular"
chrome.get('https://www.magazineluiza.com.br/')

tempo.sleep(1)

# Irá acessar o elemento pelo ID 'input-search' (campo de pesquisa)
# .send_keys() - Irá digitar no elemento
chrome.find_element(By.ID, 'input-search').send_keys(pesquisa)

# Tempo de espera após executar (1 segundo)
tempo.sleep(1)

# Pressiona ENTER
teclado.press('enter')

# Tempo de espera após executar (20 segundos)
tempo.sleep(20)

# Variável produtos recebe elementoS (find_elements)
# Pesquisamos por classe (CLASS_NAME), 'BCSuy' é o nome da classe encontrada no site 
# O nome da classe ('BCSuy') pode ser alterado com o tempo
produtos = chrome.find_elements(By.CLASS_NAME, 'BCSuy')

# Lista que irá conter as linhas (cada indice será referente a um produto) com informações do arquivo Excel
lista_dataFrame = list()

for item in produtos:
    
    # Criando as variáveis que irão receber as informações dos produtos
    nome_produto = preco_produto = url_produto = ''
    
    if not nome_produto:
        
        # nome_produto recebe elementO (find_element)
        # Pesquisamos por classe (CLASS_NAME), 'sc-kOjCZu' é o nome de uma das classes encontrada no site 
        # classes 'sc-kOjCZu enKhKW'
        # O nome da classe ('sc-kOjCZu') pode ser alterado com o tempo
        nome_produto = item.find_element(By.CLASS_NAME, 'sc-kOjCZu').text
        
        #print(nome_produto)
        
    if not preco_produto:
        
        # preco_produto recebe elementO (find_element)
        # Pesquisamos por classe (CLASS_NAME), 'sc-kDvujY' é o nome de uma das classes encontrada no site 
        # classes 'sc-kDvujY jDmBNY sc-ehkVkK kPMBBS'
        # O nome da classe ('sc-kDvujY') pode ser alterado com o tempo
        preco_produto = item.find_element(By.CLASS_NAME, 'sc-kDvujY').text
        
        #print(preco_produto)
    
    
    if not url_produto:
        
        # url_produto recebe elementO (find_element)
        # Pesquisamos pela tag name (TAG_NAME), 'a' é a tag name (link)
        # Pegamos o atributo 'href' (URL)
        url_produto = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        #print(url_produto)
        
    # Variável contendo cada produto
    # Será separado por "_" para facilitar na formatação do Excel
    linha = nome_produto + ';' + preco_produto + ';' + url_produto
    
    # Inserindo protudo na lista
    lista_dataFrame.append(linha)
    

# Cria e Prepara o arquivo excel usando o XLSXWRITER
# Irá criar um arquivo xlsx com o nome da pesquisa inserida no input
# Será substituido os espaços ' ' por '_'
pesquisa = pesquisa.replace(' ', '_').lower() + '.xlsx'
arqExcel = pandas.ExcelWriter(pesquisa, engine='xlsxwriter')

#DATAFRAME recebe pandas.DataFrame
# Passando a lista com as linhas
# columns (columns=['#_Produto_Preco_URL']) irá receber o NOME da COLUNA do arquivo EXCEL
dataFrame = pandas.DataFrame(lista_dataFrame, columns=['#_Produto_Preco_URL'])
  
# Na variável dataFrame, vou passar o arquivo EXCEL que preparamos
# sheet_name é o nome da planilha
# index=True, significa que estou autorizando a colocar o 
# index (linhas na tabela) (0, 1, 2, 3...)
# Nome da planilha será o nome da pesquisa
dataFrame.to_excel(arqExcel, sheet_name=pesquisa.replace(' ','_'), index=True)

arqExcel.save()  

print('\nPrograma encerrado\n')


      