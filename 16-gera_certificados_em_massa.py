from docx import Document
from docx.shared import Pt

from openpyxl import load_workbook


# Variável recebendo o caminho do arquivo EXCEL
doc_excel = 'alunos.xlsx'

# Carrega o arquivo doc_excel na memória como um objeto Workbook do openpyxl
# Esse objeto permite acessar as planilhas, linhas e células contidas no arquivo do Excel.
planilha_excel = load_workbook(doc_excel)

# Seleciona a "planilha" / "aba" / "sheet"
sheet = planilha_excel['Nomes']


# Função que irá alterar o nome no documento
def altera_nome(nome_aluno, documento, formatacao):
    """
    Altera o nome do aluno no Documento WORD e salva
    
    nome_aluno  - Nome do aluno contido na linha do EXCEL
    documento - Documento WORD
    formatacao - Formatação do texto 
    """

    # Loop utilizado para percorrer o documento Word
    for paragrafo in documento.paragraphs:
        # Para cada paragrafo em paragrafo:
        
        # Se encontrar '@nome' em paragrafo.text
        if '@nome' in paragrafo.text:
            
            # Substitui '@nome' pelo nome contido na linha do EXCEL
            paragrafo.text = nome_aluno.title()
            
            # Variável recebendo nossa formatação de texto
            fonte = formatacao.font
            
            # Informando o nome da fonte
            fonte.name = 'Calibri (Corpo)'
            
            # Informando o tamanho da fonte
            fonte.size = Pt(24)
    
    
    # Substituindo ' ' por '-' e alterando para lower
    nome_aluno = nome_aluno.replace(' ', '_').lower()

    # Local onde será salvo os certificados
    caminho = 'C:\\Users\\marco\\Downloads\\Cursos\\RPA Automação\\Curso\\Certificados\\' + nome_aluno + '.docx'
    
    # Salvando o arquivo com o nome do aluno
    documento.save(caminho)


# Função que "pega" o nome no arquivo EXCEL
def pega_nome(aba):
    """
    Pega o nome na planilha do EXCEL
    
    aba - "planilha" / "aba" / "sheet"
    """
    
    # Loop para percorrer a planilha do EXCEL
    # Inicia na linha 2 vai até len da planilha +1
    # sheet['A'] é referente a colua "A" da planilha
    for linha in range(2, len(aba['A']) + 1):
        
        # Variável recebendo o arquivo WORD
        # "Abre" o arquivo
        doc = Document('certificado.docx')

        # Seleciona o estilo (fonte)
        formatacao = doc.styles['Normal']
        
        # Variável recebendo o nome do aluno
        # A%s - Estou convertendo p texto
        # Passando linha por linha 
        nome = aba['A%s' % linha].value
        
        
        # Chama a função que altera e salva
        altera_nome(nome, doc, formatacao)


# Chama a função que irá pegar o nome do aluno e iniciar o programa
pega_nome(sheet)


print('Certificados emitidos com sucesso!')

