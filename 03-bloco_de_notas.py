import pyautogui


# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Pressiona duas teclas juntas
pyautogui.hotkey('win', 'r')

# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Digita notepad para abrir o Bloco de Notas
pyautogui.typewrite('notepad')

# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Pressiona ENTER
pyautogui.press('enter')

# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Insere o texto dentro do Bloco de Notas
pyautogui.typewrite('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nQuisque in metus sed sapien ultricies pretium a at justo. \nMaecenas luctus velit et auctor maximus.', 
                    interval=0.05)

# Pega a janela que está ativa
janela = pyautogui.getActiveWindow()

# Tempo de espera após executar (2 segundos)
pyautogui.sleep(2)

# Fecha a janela
janela.close()

# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Pressiona "tab"
# Não quero salvar o arquivo
pyautogui.press('tab')

# Tempo de espera após executar (1 segundo)
pyautogui.sleep(1)

# Pressiona enter
pyautogui.press('enter')

print('Automação executada com sucesso!')

