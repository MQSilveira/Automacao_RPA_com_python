from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui

# from time import sleep

# É NECESSÁRIO INSTALAR A BIBLIOTECA XlsxWriter
#   pip install XlsxWriter

# Seleciona o navegador (Chrome)
chrome = webdriver.Chrome()

# Site para extrair os dados
chrome.get('https://rpachallengeocr.azurewebsites.net/')


# Navegador continua fechando sozinho
# Criei um sleep para coder carregar a página e copiar a tabela
# sleep(5)

# Input solicitando para teclar qualquer tecla para prosseguir
# O navegador é fechado em seguida
input("\nPressione qualquer tecla para fechar o navegador\n")

# Contador de páginas
pagina = 1

lista = list()

while pagina < 4:
    
    # Variável está recebendo o XPATH da tabela
    # XPath é a linguagem usada para localizar nós em um documento XML
    # No site, acessar o Inspecionar, localizar a tabela (<table>),
    # Na linha ta tabela (<table id="tableSandbox" class=...>) BT direito, copy, copy Xpath ('//*[@id="tableSandbox"]')
    tabela_site = chrome.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # Variável recebendo uma linhas (tr)
    linhas = tabela_site.find_elements(By.TAG_NAME, 'tr')

    # Variável recebendo colunas (td)
    colunas = tabela_site.find_elements(By.TAG_NAME, 'td')
    
    for linhaAtual in linhas:

        print(linhaAtual.text)
        
        # Adicionando o objeto/texto na tabela
        lista.append(linhaAtual.text)
    
    # Variável utilizada para apertar no "botão" PRÓXIMO
    proximo = chrome.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    # Aguarda 2 segundos para carregar a próxima página
    pyautogui.sleep(2)
    
    pagina += 1
    
    
# dados_site será o nome do arquivo Excel
# engine='xlsxwriter' - xlsxwriter é a biblioteca que quero usar
arqExcel = pd.ExcelWriter('dados_site.xlsx', engine='xlsxwriter')

# Salva/Cria o arquivo Excel
arqExcel.save()

#DATAFRAME recebe pandas.DataFrame
# Passando a lista com as linhas
# columns irá receber o NOME da COLUNA do arquivo EXCEL
dataFrame = pd.DataFrame(lista, columns=['Nome_Coluna'])

# Preparo o arquivo excel usando o XLSXWRITER
arqExcel = pd.ExcelWriter('dados_site.xlsx', engine='xlsxwriter')

# Na variável dataFrame, vou passar o arquivo EXCEL que preparamos
# sheet_name é o nome da planilha
# index = True, significa que estou autorizando a colocar o 
# index (linhas na tabela) (0, 1, 2, 3...)
dataFrame.to_excel(arqExcel, sheet_name='Planilha_01', index=True)

# Salva o arquivo Excel
arqExcel.save()


# ARQUIVO EXCEL
"""
	Nome_Coluna
0	# ID Due Date Invoice
1	1 lstunzgttpjxzngz6uxhb 25-01-2023
2	2 4759sx6munxzhjkjp6w0n 20-04-2023
3	3 ix7ll45antnk2sgprvdrs 24-01-2023
4	4 9vgegmel2ted3etzp9ca2 28-12-2022
5	# ID Due Date Invoice
6	5 b36hw6dx0rby8zznazzhcm 26-01-2023
7	6 bapnpg0872visml6fukadp 13-04-2023
8	7 y8luq9p0jxobt7j1z27u 07-03-2023
9	8 2rker1vwovikzap90xszms 01-01-2023
10	# ID Due Date Invoice
11	9 zi0r77adizpidb0pgj1e9e 11-03-2023
12	10 92cdujx18ua1n54rje6o7z 09-03-2023
13	11 fii529l6jhol1yjma6lyx 24-01-2023
14	12 9is25oarjv8wfb0kkdyr7 25-02-2023
"""

