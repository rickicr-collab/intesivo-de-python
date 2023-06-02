import pyautogui
import time
import pyperclip


# pyautogui.click - > vai clicar com mouse
# pyautogui.write - > vai escrever um texto
# pyautogui.press - > vai pressionar uma tecla
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

#Passo 1: acessar sistema da empresa
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.click(x = 1000, y = 34)
pyautogui.write("http://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("Enter")
time.sleep(5)

#Passo 2: Fazer login no sistema
pyautogui.click(x = 650, y = 342)
pyautogui.write("meu login")

pyautogui.click(x = 761, y = 414)
pyautogui.write("minha senha")

pyautogui.click(x = 644, y = 490)

time.sleep(5)
#Passo 3: baixar a base de dados
pyautogui.click(x = 404, y = 347)
pyautogui.click(x = 495, y = 328)
pyautogui.click(x = 624, y = 563)


# Passo 4: Calcular os Indicadores
import pandas as pd

# importar a base de dados
tabelas = pd.read_csv(r"C:\Users\Ricardo\Downloads\Compras.csv", sep = ";")
print(tabelas)
# calculo dos indicadores 
# total gasto -> somar a coluna valor final
total_gasto = tabelas["ValorFinal"].sum()

# quantidade -> somar a coluna quantidade
quantidade = tabelas["Quantidade"].sum()

# preço médio -> total gasto / quantidade
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

# passo 5: Enviar email para chefe

# entrar no email
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")

time.sleep(5)

# clicar em escrever
pyautogui.click(x= 94, y= 175)
pyautogui.write("ricardo.rosendo2@gmail.com")
 
# preencher o email
pyautogui.write("ricardo.rosendo2@gmail.com")
pyautogui.press("tab") # seleciona o email
  
pyautogui.press("tab") # passa para o campo assunto
pyperclip.copy("relátorio de Compras")
pyautogui.hotkey("crtl", "v")
 
pyautogui.press("tab") # passa para o corpo do email
 
texto = f'''
Prezados,
Segue o relátorio de compras

Total Gasto: R$ {total_gasto:,.2f}
Quantidade: {quantidade:,}
Preço Medio: R$ {preco_medio:,.2f}

Qualquer duvida estou a disposição
 
Att.
ricardo do Python
 '''
pyperclip.copy(texto)
pyautogui.hotkey("crtl", "v")

# Enviar
