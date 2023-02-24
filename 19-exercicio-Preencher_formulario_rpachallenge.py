"""
1 - Acessar o site https://www.rpachallenge.com/.
2 - Preencher todos os campos do formulário utilizando as informações contidas no arquivo 
    excel disponível para download a mesma página (https://www.rpachallenge.com/).
Obs 1: Os campos alteram a ordem após clicar em submit.
Obs 2: O ID/NAME dos campos mudam após clicar em submit.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

import pyautogui

from openpyxl import load_workbook


# Função que irá preencher os formulários
def preenche_formulario(aba, navegador):
    """
    Função criada para preencher os formulários do exercício.
    Link do exercício: https://www.rpachallenge.com/

    Args:
        aba (class 'openpyxl.worksheet.worksheet.Worksheet'): "planilha" / "aba" / "sheet"
        navegador (class 'selenium.webdriver.chrome.webdriver.WebDriver'): Objeto contendo a Classe do navegador
    """

    # Loop para percorrer a planilha do EXCEL
    # Inicia na linha 2 vai até len da planilha +1
    # aba['A'] é referente a colua "A" da planilha
    for linha in range(2, len(aba['A']) + 1):
        
        # Verifica se aba['A'] está vazio.
        # Se estiver vazio, irá parar a execução
        if aba['A%s' % linha].value is None:
            break
        
        # Inserindo o campo da tabela em seu respectivo campo do formulário
        # A%s - Estou convertendo p texto
        # Passando linha por linha
        pyautogui.sleep(1)

        # Localiza o campo
        # //*[@] 

        # Nome
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(aba['A%s' % linha].value)

        pyautogui.sleep(1)

        # Sobrenome
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(aba['B%s' % linha].value)

        pyautogui.sleep(1)
        
        # Empresa
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(aba['C%s' % linha].value)
        
        pyautogui.sleep(1)

        # Cargo
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(aba['D%s' % linha].value)

        pyautogui.sleep(1)
        
        # Endereço
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(aba['E%s' % linha].value)

        pyautogui.sleep(1)

        # Email
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(aba['F%s' % linha].value)

        pyautogui.sleep(1)
        
        # Telefone
        navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(aba['G%s' % linha].value)

        pyautogui.sleep(1)

        # Submit
        navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
    

# Carrega o arquivo EXCEL na memória como um objeto Workbook do openpyxl
# Esse objeto permite acessar as planilhas, linhas e células contidas no arquivo do Excel.
doc_excel = load_workbook('challenge.xlsx')

# Seleciona a "planilha" / "aba" / "sheet"
sheet = doc_excel['Sheet1']

# Navegador
chrome = webdriver.Chrome()

# Abre a página
chrome.get('https://www.rpachallenge.com/')

pyautogui.sleep(3)

# Clica em START 
chrome.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

preenche_formulario(sheet, chrome)

pyautogui.sleep(1)

print('Todas as tabelas foram preenchidas')

