import tabula

lista_tabelas = tabula.read_pdf('ResultadoVale.pdf', pages=11)
print(len(lista_tabelas))

'''for tabela in lista_tabelas:
    display(tabela)'''

lista_tabelas2 = tabula.read_pdf('ResultadoVale.pdf', pages=10)
print(lista_tabelas2)
# display(lista_tabelas2[0])

lista_tabelas2 = tabula.read_pdf('ResultadoVale.pdf', pages=10)
tabela = lista_tabelas2[0]
tabela.columns = tabela.iloc[0] # iloc pega a primeira linha da tabela.
tabela[[0, 1]] = tabela["Variação percentual"].str.split(" ", expand=True)
# tabela = tabela.drop(0,axis=0) #excluí a linha 0
tabela = tabela[1:9]
tabela = tabela.set_index('R$ milhões')  # Essa coluna passa a ser o index da tabela.
tabela.columns = tabela.iloc[0]
tabela = tabela[~tabela.index.isna()] # Retorna toda a tabela tirando apenas o indice NaN
tabela = tabela.drop('1T21/4T20 1T21/1T20', axis = 1) # Excluí a coluna 
# display(tabela)

