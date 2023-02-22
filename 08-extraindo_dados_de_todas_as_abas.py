from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui


# É NECESSÁRIO INSTALAR A BIBLIOTECA XlsxWriter
#   pip install XlsxWriter


# Seleciona o navegador (Chrome)
chrome = webdriver.Chrome()

# Site para extrair os dados
chrome.get('https://rpachallengeocr.azurewebsites.net/')


# Navegador continua fechando sozinho
# Criei um sleep para poder carregar a página e copiar a tabela
pyautogui.sleep(2)

# Input solicitando para teclar qualquer tecla para prosseguir
# O navegador é fechado em seguida
# input("\nPressione qualquer tecla para fechar o navegador\n")
# utilizando o SLEEP, a execução entrou no WHILE e o mesmo não deixou fechar

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

        # Print no terminal para averiguar se está OK
        print(linhaAtual.text)
        
        # Adicionando o objeto/texto na tabela
        lista.append(linhaAtual.text)
    
    # Apertar no "botão" PRÓXIMO
    chrome.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    # Aguarda 2 segundos para carregar a próxima página
    pyautogui.sleep(2)
    
    pagina += 1
    
 
#DATAFRAME recebe pandas.DataFrame
# Passando a lista com as linhas
# columns (columns=['Nome_Coluna']) irá receber o NOME da COLUNA do arquivo EXCEL
dataFrame = pd.DataFrame(lista, columns=['# ID Due_Date'])

# Cria e prepara o arquivo excel usando o XLSXWRITER
# dados_site será o nome do arquivo Excel
# engine='xlsxwriter' - xlsxwriter é a biblioteca que quero usar
arqExcel = pd.ExcelWriter('dados_site.xlsx', engine='xlsxwriter')

# Na variável dataFrame, vou passar o arquivo EXCEL que preparamos
# sheet_name é o nome da planilha
# index=True, significa que estou autorizando a colocar o 
# index (linhas na tabela) (0, 1, 2, 3...)
# index=False para uma formatação melhor no EXCEL
dataFrame.to_excel(arqExcel, sheet_name='Planilha_01', index=False)

# Print informando que o arquivo foi criado com sucesso
print('\nArquivo criado com sucesso')

# Salva o arquivo Excel
arqExcel.save()


# FORMATAR O ARQUIVO EXCEL
"""
# No arquivo Excel:
    Excluiras linhas com titulos repetidos (# ID Due Date Invoice)
    
    Selecionar a coluna "A"
    Menu "Dados"
    Texto para Colunas
    Opção "Delimitado" / Avançar
    Escolher a opção "Espaço"
    Concluir
"""

# ARQUIVO EXCEL ANTES DA FORMATAÇÃO
"""
# ID Due_Date
# ID Due Date Invoice
1 jboq0dy9gaomqsqahih8r 04-01-2023
2 gvrwzf8wxoc06cpccok5edh 20-01-2023
3 af1unwjsatpwin3cda9i48 15-04-2023
4 nj1seel7w9a5ii2e5qeu8p 01-01-2023
# ID Due Date Invoice
5 cjme4tcpn3p99qvkmp37f 12-04-2023
6 fuxixaj7c5mwjlbsvjbhcd 10-02-2023
7 5m1yykdncw94mzx9gu0n1s 02-02-2023
8 ofpl1685lco070153hc07bi 27-12-2022
# ID Due Date Invoice
9 qradbljb8fo1seetx9uinm 06-04-2023
10 ywwig5knhdmwjyvio8ffg 11-04-2023
11 c0kt6dk34osqoyph4jmkqc 27-03-2023
12 bq39260ob3q8qcvuqg50j4 09-04-2023
"""


# ARQUIVO EXCEL APÓS FORMATAÇÃO
"""
#	ID	                    Due_Date
1	gjede72k15apcg2ly8l39	10/04/2023
2	fkh4zya5dfi4kyqmnewnkd	18/01/2023
3	7yxpaiuawfkc1et1pafwib	12/03/2023
4	y6649c63sh6lhibu41vd3	09/02/2023
5	vycf700ukovosnaeftbor	02/04/2023
6	x48bivu4u2oelsb0a816ru	21/01/2023
7	pdc0fnmsbe8iry1rm064ed	18/01/2023
8	bisvr1c2qfwp5ijxgqfh2	03/01/2023
9	tohf63z832en5q082p9h4l	08/04/2023
10	sw5r9fa2czyl91or0kefq	05/01/2023
11	6grxt4mmfhglorh8ornfsg	21/04/2023
12	2dw4yklfbcqkcg7lt418f9	26/03/2023
"""

