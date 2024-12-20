import tabula

lista_tabelas = tabula.read_pdf('ResultadoVale.pdf', pages = "10")
print(len(lista_tabelas))

lista_tabelas2 = tabula.read_pdf('ResultadoVale.pdf', pages = 10)
tabela = lista_tabelas2[0]
tabela.columns = tabela.iloc[0] # Aqui eu pego a primeira linha da tabela para ser o cabeçalho dela. 
tabela[[0, 1]] = tabela['Variação percentual'].str.split(' ', expand = True) # Criação de duas colunas onde eu preciso  colocar o expand = True para que as colunas sejam realmente divididas, sem ele seria criada uma lista de strings. 
tabela = tabela.drop(0, axis = 0) # Aqui eu excluí a linha 0, conforme eu aprendi na aula de pandas básico
tabela = tabela.drop('Variação percentual', axis = 1) # Aqui eu excluí a coluna 'Variação percentual'. O Axis = 1 usei para especificar que a operação deve ser realizada na coluna e não na linha. 
tabela = tabela[1:8]
tabela = tabela.set_index('R$ milhões')
tabela.columns = ['1T21', '4T20', '1T20', '1T21/4T20', '1T21/1T20']
# display(tabela)


# Se o método acima não conseguir ler minha tabela toda, posso utilizar esses dois métodos abaixo:
# Lattice
lista_df = tabula.read_pdf('ResultadoVale.pdf', pages = 10, lattice = True)
# display(lista_df[0])

print('*' * 100)

# guess
lista_df = tabula.read_pdf('ResultadoVale.pdf', pages = 10, guess = False)
# display(lista_df[0])