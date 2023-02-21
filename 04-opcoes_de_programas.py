# -*- coding: utf-8 -*-
import pyautogui as opcao


def excel():
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    print('Opção escolhida foi EXCEL')
    
    # Pressiona duas teclas juntas
    opcao.hotkey('win', 'r')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)

    # Digita notepad para abrir o Bloco de Notas
    opcao.typewrite('excel')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    # Pressiona "enter" para fechar a notificação de ativação do OFFICE
    opcao.press('enter')
    
    # Tempo de espera após executar (5 segundos)
    opcao.sleep(5)
    
    # Pressiona "enter" para abrir uma planilha nova
    opcao.press('enter')
    
    # Tempo de espera após executar (5 segundos)
    opcao.sleep(5)
    
    # Insere o texto
    opcao.typewrite(' Escolhi a opcao EXCEL', interval=0.05 )
    

def word():
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    print('Opção escolhida foi WORD')
    
    # Pressiona duas teclas juntas
    opcao.hotkey('win', 'r')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)

    # Digita notepad para abrir o Bloco de Notas
    opcao.typewrite('winword')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    # Pressiona "enter" para fechar a notificação de ativação do OFFICE
    opcao.press('enter')
    
    # Tempo de espera após executar (5 segundos)
    opcao.sleep(5)
    
    # Pressiona "enter" para abrir uma planilha nova
    opcao.press('enter')
    
    # Tempo de espera após executar (10 segundos)
    opcao.sleep(10)
    
    # Insere o texto
    opcao.typewrite(' Escolhi a opcao WORD', interval=0.05)
  

def notepad():
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    print('Opção escolhida foi BLOCO DE NOTAS')
    
    # Pressiona duas teclas juntas
    opcao.hotkey('win', 'r')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)

    # Digita notepad para abrir o Bloco de Notas
    opcao.typewrite('notepad')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
        
    # Pressiona "enter" para abrir o Bloco de Notas
    opcao.press('enter')
    
    # Tempo de espera após executar (1 segundo)
    opcao.sleep(1)
    
    # Insere o texto
    opcao.typewrite('Escolhi a opcao BLOCO DE NOTAS', interval=0.05)
  

janela = opcao.confirm('Escolha uma opcao:',
                       buttons=['Excel', 'Word', 'Bloco de Notas'])


if janela == 'Excel':
    
    excel()
    
elif janela == 'Word':
    
    word()
    
elif janela == 'Bloco de Notas':
    
    notepad()
    
else :
    
    print('O programa foi fechado')
    
