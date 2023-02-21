import pyautogui as mouse
import pyautogui as tempo
# As duas importações são iguais, porém os "apelidos" são diferentes
# Isso auxilia na interpretação


# Tempo de espera após executar (1 segundo)
tempo.sleep(1)

# Irá mostrar a posição em que o cursor do mouse edstava 
#print(mouse.position())
# Point(x=42, y=1042)

# Podemos utilizar o mouse.click() direto
# Porém teremos a impressão do mouse se "mexendo"

# Irá clicar com o botão principal do mouse 
mouse.click(42, 1042)

# Tempo de espera após executar (1 segundo)
tempo.sleep(1)

# Irá pesquisar "calc" (calculadora)
# typewrite permite escrever
mouse.typewrite('chrome')

# Tempo de 'espera após executar (1 segundo)
tempo.sleep(1)

# Pressiona ENTER
mouse.press('enter')

# Tempo de 'espera após executar (3 segundos)
tempo.sleep(3)

# Irá digitar "valor do dolar hoje"
# typewrite permite escrever
mouse.typewrite('valor do dolar hoje')

# Pressiona ENTER
mouse.press('enter')
