from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

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


# Variável está recebendo o XPATH da tabela
# XPath é a linguagem usada para localizar nós em um documento XML
# No site, acessar o Inspecionar, localizar a tabela (<table>),
# Na linha ta tabela (<table id="tableSandbox" class=...>) BT direito, copy, copy Xpath ('//*[@id="tableSandbox"]')
tabela_site = chrome.find_element(By.XPATH, '//*[@id="tableSandbox"]')

# Variável recebendo uma linhas (tr)
linhas = tabela_site.find_elements(By.TAG_NAME, 'tr')

# Variável recebendo colunas (td)
colunas = tabela_site.find_elements(By.TAG_NAME, 'td')


lista = list()

for linhaAtual in linhas:

    print(linhaAtual.text)
    
    # Adicionando o objeto/texto na tabela
    lista.append(linhaAtual.text)
    

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
1	1 9c9ykzyq0j4j8mm2fc5cx 15-04-2023
2	2 cem4e9io69vspo2hyphvx 27-02-2023
3	3 jzuny2uomds3t17vmb4b 01-01-2023
4	4 hpv1cdzmfre04zjz36qtj47 27-01-2023
"""
