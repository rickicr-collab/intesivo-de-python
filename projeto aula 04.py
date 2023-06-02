#   importando o banco de dados 
import pandas as pd

tabela = pd.read_csv("dadosveiculos.csv")
print(tabela)
# imprimindo a relação de dados dentro do banco de dados e quais informaçoes estão incorretas ou vazias para realizar tratamento de limpeza nos dados 
print(tabela.info())

# Analise exploratória
    # usandno a função corr() para verificar a correlaçao das informações dentro da tabela 
    # para realizar a pesquisa de apenas uma unica coluna em relaçao as linhas é so realizar a adição da colina emtre chaves junto coma função
    # usando esse formato {{"nome da coluna "}} é possivel deixar a coluna com layout mais agradavel
print(tabela.corr()[["barrels08"]])
    # sobre correlação ( proporçoes baseados nos valores 0 -> 1 quanto mais proximo do 0 menos proprocional é / quanto mais proximo do 1 mais proprocional é )
    
# opcional criando graficos usando:
    #seaborn 
    # matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# criando o grafico 
    # usando o paramentor cmap= atribui um valor de cores para o grafico dependendo do tipo de grafico foi atribuido para a construção como por exemplo heatmap(mapa de calor)
    # usando o paramentro annot= atribui as informaçoes de cada seção no grafico apresentado as correlaçoes segundo as informacoes (annot ->2 vem de annotacoes ou anotar)
sns.heatmap(tabela.corr()[["barrels08"]], cmap= "Blues", annot = True)
# exibindo o grafico
plt.show()

# Criando modelagem + algaritmo ( inteligencia Artifical)

    # criação da IA
    # - separar a base de dados em x e y
y = tabela["Model"]
x = tabela.drop("Model", axis = 1)
    # Treino da IA
    # separando dados de treino e dados de teste para inteligencia artificial
    # usando o parametro test_size= atribuisse o quantidade de dados a ser usados pela inteligecia artificial para teste 
    # parametro random_state=
from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# criação e treino da IA

# importa a inteligencia artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# criar a ineligencia artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treinar inteligencia artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# previsão

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))

# Interpretação dos resultados 

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar['y_teste'] = y_teste
tabela_auxiliar["Previsoes Arvore de Decisão"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes da Regressão Linear"] = previsao_regressaolinear

sns.lineplot(data=tabela_auxiliar)
plt.show()

#ordendnando o grafico de acordo com os valores 

'''usando seaborn
e usando matplotlib'''

# Opçional 
    # criando uma variavel
    # correlação = tabela.corr()[["barrels08"]]
    # correlacao = correlação.sort_values()
    # sns.heatmap(correlação,cmap= "Blues", annot = True)
    # plt.show()