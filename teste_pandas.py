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

# Resumo da visualização de dados simples e úteis:
''' - head (só aparece as 5 primeiras linhas por padrão)
    display(vendas_df.head()); display(vendas_df.head(10)) já aqui apareceria as 10 primeiras linhas.
    - shape(mostra quantas linhas e colunas têm na inha tabela)
    print(vendas_df.shape);
    - describe (ele me dá um resumo de toda a tabela)
    display(vendas_df.describe())'''

# Métodos de edição de um dataframe:
'''Digamos que queiramos olhar apenas a coluna de produtos, para saber quais produtos eu tenho nela:'''
produtos = vendas_df[['Produto', 'ID Loja']] # Quando eu pego só uma coluna da minha tabela não é um DF, por isso não tem "df" na variável produtos.
print(produtos)

# Método .loc
'''-pegar uma linha;
   -pegar linhas de acordo com alguma condição
   -pegar linhas e colunas específicas
   -pegar 1 valor específico'''

# Pegar uma linha
print(vendas_df.loc[1])
print(vendas_df.loc[1:5])

# Pegar linhas que correspondem a uma condição
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'] # Armazenei nessa variável.

# Pegar várias linhas e coluna. Lembrando que o padrão do loc é .loc[linhas, colunas]
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
print(vendas_norteshopping_df)

# Pegar um valor específico
print(vendas_df.loc[1,"Produto"])

# Método adicionar nova coluna
'''- a partir de uma coluna que já existe;
   - crio uma coluna nova;'''

# A partir de uma coluna que já existe (digamos que queremos criar uma coluna comissão de qto o vendedor ganha 5%)
'''vendas_df['Comissão'] =  Se eu fizer isso a coluna comissão, se já existir, vai receber um novo valor. Se não existir, ele vai criar'''
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05

# Criar uma coluna nova:
vendas_df['Imposto'] = 0 # Se for uma tabela muito grande vai dá problema, daí o pandas indica fazer utilizando o .loc como no exemplo abaixo:
vendas_df.loc[:, 'Imposto'] = 0 # É menos custosa pra exacutar 
print(vendas_df)

# Adicionar linhas
vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')
vendas_df = pd.concat([vendas_df, vendas_dez_df], ignore_index=True) # Lembre-se: como vem linhas vazias, vc poderia colocar primeiro as linhas depois as colunas ou posso colocar as colunas "comissão" e "imposto" também na tabela vendas-dez.xlsx
print(vendas_df)

# Método de excluir linhas e colunas:
vendas_df = vendas_df.drop('Imposto', axis=1) # 0 é o eixo da linha e 1 o eixo da coluna
print(vendas_df)
vendas_df = vendas_df.drop(0, axis = 0) # excluí a linha 0
print(vendas_df)

# Tratar valores vazios:
# Deletar linhas e colunas completamente vazias
vendas_df = vendas_df.dropna(how='all') # está excluindo as linhas onde todos os valores são vazios. Se eu quiser coluna, basta adicionar o eixo 1 (axis=1), conforme exemplo:
vendas_df = vendas_df.dropna(how='all', axis=1)

# Se tiver pelo menos um valor vazio, eu quero excluir:
vendas_df = vendas_df.dropna()

# Preencher valores vazios com a médias da coluna:
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(0) # Se eu preencher o fillna, nesse caso 0, ele substituirá todos os valores de NA por 0, e assim pelo oq estiver argumentado.
vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean()) # Nesse caso substituirá pela média da coluna comissão. 
print(vendas_df)

# Preencher com o último valor:
vendas_df = vendas_df.ffill() # Vai preencher com o primeiro (FIRST) valor acima dele.

# Método Value Counts:
'''Qual foi o faturamento total? Qual foi o faturamento por loja? Quantas transações eu tive poe loja(quantas linhas)? Quantas linhas eu tive nessa tabela?'''
transacao_por_loja = vendas_df['ID Loja'].value_counts()
print(transacao_por_loja)

# Método Group by:
'''Digamos que eu queira saber o faturamento de cada um dos produtos'''
# faturamento_por_produto = vendas_df.groupby('Produto').sum() # Nesse caso eu estou somando toda a tabela, com todas as colunas. Entretanto tenho um problema aqui, não consigo somar a coluna Data, ocorrendo um erro. Para solucionar isso há duas opções: ou eu excluo a coluna Data ou seleciono(1), manualmente, quais colunas eu quero que ele mostre(2).
faturamento_por_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum() # Opção 2
# faturamento_por_produto = vendas_df.select_dtypes(exclude=['datetime']).groupby('Produto').sum() # Opção 1
'''Nesse caso se eu trocar o sum pelo mean eu pegaria a média dos produtos por loja'''
print(faturamento_por_produto)

# Método de mesclar 2 dataframes: como eu vou procurar as informações de uma tabela em dentro de outra tabela?
gerentes_df = pd.read_excel('Gerentes.xlsx')
vendas_df = vendas_df.merge(gerentes_df) # O pandas reconhece automaticamente as colunas já existentes na tabela anterior.
print(vendas_df)
