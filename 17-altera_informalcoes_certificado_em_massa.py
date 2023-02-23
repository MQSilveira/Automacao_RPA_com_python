from docx import Document
from docx.shared import Pt

from openpyxl import load_workbook


# Variável recebendo o caminho do arquivo EXCEL
doc_excel = 'dados_alunos.xlsx'

# Carrega o arquivo doc_excel na memória como um objeto Workbook do openpyxl
# Esse objeto permite acessar as planilhas, linhas e células contidas no arquivo do Excel.
planilha_excel = load_workbook(doc_excel)

# Seleciona a "planilha" / "aba" / "sheet"
sheet = planilha_excel['Nomes']


# Função que irá alterar o os dados do documento Word
def altera_dados(dados_aluno, documento, formatacao):
    """
    Altera os dados do aluno (nome, dia, mês, ano, curso, instrutor) 
    no Documento WORD e salva
    
    dados_aluno  - Dicionário contendo dados do aluno contido na linha do EXCEL
    documento - Documento WORD
    formatacao - Formatação do texto 
    """

    # Loop utilizado para percorrer o documento Word
    for paragrafo in documento.paragraphs:
        # Para cada paragrafo em paragrafo:
        
        # Altera Nome do Aluno
        # Se encontrar '@nome_alino' em paragrafo.text
        if '@nome_aluno' in paragrafo.text:
            
            # Substitui '@nome' pelo nome contido na linha do EXCEL
            paragrafo.text = dados_aluno['nome'].title()
            
            # Variável recebendo nossa formatação de texto
            fonte = formatacao.font
            
            # Informando o nome da fonte
            fonte.name = 'Calibri (Corpo)'
            
            # Informando o tamanho da fonte
            fonte.size = Pt(24)
            
            
        # Altera o Conteudo do Certificado
        # Irá inserir as informações do Aluno no conteúdo
        if '@conteudo' in paragrafo.text:
            
            # Variável que irá conter as alterações
            conteudo = f'Concluiu com sucesso o curso de {dados_aluno["curso"].title()}, como carga horária de 20 horas, promovido pela escola de Cursos Online em {dados_aluno["dia"]} de {dados_aluno["mes"]} de {dados_aluno["ano"]}.'

            # Insere a variável contendo as alterações
            paragrafo.text = conteudo
            
            # Variável recebendo nossa formatação de texto
            fonte = formatacao.font
            
            # Informando o nome da fonte
            fonte.name = 'Calibri (Corpo)'
            
            # Informando o tamanho da fonte
            fonte.size = Pt(24)
        
        
        #Altera Instrutor 
        # Se encontrar '@instrutor' em paragrafo.text
        if '@instrutor' in paragrafo.text:
            
            # Substitui '@instrutor' pelo mês contido na linha do EXCEL
            paragrafo.text = f'{dados_aluno["instrutor"].title()} - Instrutor'
            
            # Variável recebendo nossa formatação de texto
            fonte = formatacao.font
            
            # Informando o nome da fonte
            fonte.name = 'Calibri (Corpo)'
            
            # Informando o tamanho da fonte
            fonte.size = Pt(24)
            
            
    # Substituindo ' ' por '-' e alterando para lower
    dados_aluno['nome'] = dados_aluno['nome'].replace(' ', '_').lower()

    # Local onde será salvo os certificados
    caminho = 'C:\\Users\\marco\\Downloads\\Cursos\\RPA Automação\\Curso\\Certificados\\' + dados_aluno['nome'] + '.docx'
    
    # Salvando o arquivo com o nome do aluno
    documento.save(caminho)


# Função que "pega" o nome no arquivo EXCEL
def pega_nome(aba):
    """
    Pega o nome na planilha do EXCEL
    
    aba - "planilha" / "aba" / "sheet"
    """
    
    # Dicionário que irá conter os dados do aluno
    dados_aluno = dict()
    
    # Loop para percorrer a planilha do EXCEL
    # Inicia na linha 2 vai até len da planilha +1
    # sheet['A'] é referente a colua "A" da planilha
    for linha in range(2, len(aba['A']) + 1):
        
        # Variável recebendo o arquivo WORD
        # "Abre" o arquivo
        doc = Document('certificado03.docx')

        # Seleciona o estilo (fonte)
        formatacao = doc.styles['Normal']
        
        # Variável recebendo o nome do aluno, dia, mês, ano, curso, instrutor
        # A%s - Estou convertendo p texto
        # Passando linha por linha 
        # Atribuindo os dados do aluno que estão no arquivo Excel, no dicionário
        dados_aluno['nome'] = aba['A%s' % linha].value

        dados_aluno['dia'] = aba['B%s' % linha].value
        
        dados_aluno['mes'] = aba['C%s' % linha].value
        
        dados_aluno['ano'] = aba['D%s' % linha].value
        
        dados_aluno['curso'] = aba['E%s' % linha].value
        
        dados_aluno['instrutor'] = aba['F%s' % linha].value
        
        
        # Chama a função que altera e salva
        altera_dados(dados_aluno, doc, formatacao)


# Chama a função que irá pegar o nome do aluno e iniciar o programa
pega_nome(sheet)


print('Certificados emitidos com sucesso!')

