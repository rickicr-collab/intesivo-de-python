# Passo 1: Entrar na internet
from selenium import webdriver

navegador = webdriver.Chrome()

# Passo 2: Importar a base de dados

import pandas as pd

tabela = pd.read_excel("cotacoes.xlsx")
print(tabela)

# Passo 3: Para cada produto da nossa base
# Passo 4: Pegar o preço atual do produto
# Passo 5: Atualizar o preço na base de dados

# .send_keys('Meu nome é ricardo) -> escrever algo
# .click() -> clicar nele
# .get_attribute -> pegar alguma informaçõa dele

for linha in tabela.index:
    
    produto = tabela.loc[linha, "Produto"]
    # Entrar no site melhor combio: http://www.melhorcambio.com/milho-hoje
    link = f"http://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("ó", "o").replace("ã", "a").replace("á", "a").replace("ç", "c").replace("ú", "u").replace("é", "e")
    navegador.get(link)

    # pegar cotação do milho 
    cotacao = navegador.find_element('xpath', '//*[@id="cta-saibamais-1aDobra"]').get_attribute('value')
    cotacao = cotacao.replace(".", "")
    cotacao = cotacao.replace(",", ".")
    cotacao = float(cotacao)
    print(cotacao)


    # na coluna Preço atual do milho preencher cotação  do milho
    tabela.loc[linha, "Preço Atual"] = cotacao
    print(tabela)
    
# Passo 6: Decidir qual produto se deve comprar 
print(tabela)

tabela["Comprar"] = tabela["Preço Atual"] < ["Preço Ideal"]
print(tabela)

# Passo 7: Exportar a base de dados
navegador.quit()

tabela.to_excel("cotacoes_atualizado.xlsx", index = False)