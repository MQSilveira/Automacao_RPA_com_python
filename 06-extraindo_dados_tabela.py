from selenium import webdriver
from selenium.webdriver.common.by import By

# from time import sleep


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

for linhaAtual in linhas:
    print(linhaAtual.text)
    
    
# print(linhaAtual.text)
"""
# ID Due Date Invoice
1 oy6xcqbz2ek0qcpw8xrhi2n 19-01-2023
2 k7vdbp2mullv89yhqgn46 05-03-2023
3 my7cn28ipqhq5ayv7rbbrl 02-02-2023
4 u7sc1sazpeie59rorn2lbm 22-01-2023
"""

# print(linhaAtual)
"""
<selenium.webdriver.remote.webelement.WebElement (session="873c64a13e6336f04e3c3028e9ae5bdb", element="8fa10e16-f3c6-4659-b2ed-5481b890a641")>
<selenium.webdriver.remote.webelement.WebElement (session="873c64a13e6336f04e3c3028e9ae5bdb", element="94c73028-a5ea-485d-bbea-1cda841ef28c")>
<selenium.webdriver.remote.webelement.WebElement (session="873c64a13e6336f04e3c3028e9ae5bdb", element="db3ed65b-c7ba-4303-b62d-1289e5c817b5")>
<selenium.webdriver.remote.webelement.WebElement (session="873c64a13e6336f04e3c3028e9ae5bdb", element="0f9e6c5b-3812-4b23-ae54-a3ccbe7b714b")>
<selenium.webdriver.remote.webelement.WebElement (session="873c64a13e6336f04e3c3028e9ae5bdb", element="dbd8dc84-b73e-4c1a-8665-56f8d6ed168c")>
"""

