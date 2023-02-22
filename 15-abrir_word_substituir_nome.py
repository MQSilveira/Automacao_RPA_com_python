from docx import Document       # pip install python-docx
from docx.shared import Pt      # Serve para alterar o tamanho das letras


nome = str(input('Insira o nome completo do aluno: ')).strip().title()

# Variável recebendo o arquivo word
# "Abre" o arquivo
doc = Document('certificado.docx')

# Seleciona o estilo (fonte)
formatacao = doc.styles['Normal']

# Loop utilizado para percorrer o documento Word
for paragrafo in doc.paragraphs:
    # Para cada paragrafo em paragrafo:
    
    # Se encontrar '@nome' em paragrafo.text
    if '@nome' in paragrafo.text:
        
        # Substitui '@nome' pelo inserido
        paragrafo.text = nome
        
        # Variável recebendo nossa formatação de texto
        fonte = formatacao.font
        
        # Informando o nome da fonte
        fonte.name = 'Calibri (Corpo)'
        
        # Informando o tamanho da fonte
        fonte.size = Pt(24)

# Substituindo ' ' por '-' e alterando para lower
nome = nome.replace(' ', '_').lower()

# Salvando o arquivo com o nome do aluno
doc.save(f'{nome}.docx')

