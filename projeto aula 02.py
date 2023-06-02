# Passo 1: Importar a base de Dados 
import pandas as pd
import plotly.express as px

planilha = pd.read_csv("vgsales.csv", encoding = "Latin")
# Passo 2: Visualisar a Base de Dados (etápa importante)
    #Entender as informações disponiveis (informações que não te ajudam atrapalham)
    # procurar as cagadas da bases de dados 
print(planilha)
# Passo 3: Tratamento de Dados 
    #Valores no formato Errado
planilha["Year"] = pd.to_numeric(planilha["Year"], errors = "raise")
    #Valores Vazios(Preenchidos errados)
planilha = planilha.dropna()
print(planilha.info())
# Passo 4: Analise Inicial = entender como estão as vendas de videogames
print(planilha.describe())
# Passo 5: Analise Completa = sobre as vendas dos jogos no mundo
        # Criar o gráfico
for coluna in planilha.columns:
    grafico = px.histogram(planilha, x = coluna, color = 'Platform', histfunc='avg', text_auto=True, nbins=10)
        # Exibe o gráfico
    grafico.show()
    
    
# deletando colunas numa base de dados 
    # informando o nome da base de dados 
        #  - clientes.csv
    # chama o nome da planilha junto com a função drop mais o eixo a ser excluido usando a função axis como parametro
    # axis( eixo) = 0 - quando se quer excluir uma linha / 1 - quando se quer excluir uma coluna no entanto ele não edita o arquivo original
    
        # - Planilha = Planilha.drop("o nome do que se quer excluir" , axis = 0 / 1) 
        
# modificando valores na tabela 
    # Valores de formato errado
        # planilha["Year"] = pd.to_numeric(planilha["Year"], errors = "")
        # - "coerce" = força o erro a ser modificado 
        # - "raise", a análise inválida gerará uma exceção
        # - "ignore" = ignora o parametro a ser modificado
            
# Tratamento de Valores vazios 
    # Utilizando a função especial chamada dropna() o mesmo deleta todas as informaçoes com valores vazios existentes 
        # planilha = planilha.dropna()
        
# Visualzando as descriçoes da Tabela 
    # usando a função describe
        #planilha.descibe()
        
# função para realizar a media dos valores no grafico
    # utilizando a função histfunc
        #grafico = px.histogram(planilha, x = 'Platform', color = 'Platform', histfunc = 'avg')
        # avg = "average"
        
# mostrando dos dados no grafico para cada item relacionado
    #utilizando a função text_auto = True
        # grafico = px.histogram(planilha, x = 'Platform', y = 'Year', color = 'Platform', text_auto=True)

# parametro com função que mostra as divisoes realcionadas aos picos no gráfico
    # utilizando a função nbins = valor inteiro = int
        # grafico = px.histogram(planilha, x = 'Platform', color = 'Platform', histfunc='avg', text_auto=True, nbins=10)
        
# plataforma com maior vendas 
# vendas por local
# Publishermais populares 
# o gênero de ação possui mais vendas 
# no japão as vendas do nintendo DS são maiores 
# vendas em outros lugares SAT se sai melhor 
# vendas globais o NItendo DS se sai melhor 