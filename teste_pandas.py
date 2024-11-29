import pandas as pd

'''Criando um dataframe vazio
dataframe = pd.DataFrame()'''

# Criando um dataframe a partir de um dicionário:
venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor':[500, 300],
         'produto':['feijão', 'arroz'],
          'qtde':[50, 70]}
vendas_df = pd.DataFrame(venda)  # aqui eu criei um dataframe do meu dicionário venda
print(vendas_df)
# display(vendas_df) Só funciona no jupyter

# Criando dataframe a partir de uma base de dados:
vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df)

#Resumo da visualização de dados simples e úteis:
''' - head (só aparece as 5 primeiras linhas por padrão)
    display(vendas_df.head()); display(vendas_df.head(10)) já aqui apareceria as 10 primeiras linhas.
    - shape(mostra quantas linhas e colunas têm na inha tabela)
    print(vendas_df.shape);
    - describe (ele me dá um resumo de toda a tabela)
    display(vendas_df.describe())'''

