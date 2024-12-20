''' expressões regulares é um método formal de se especificar um padrão de texto. Mais detalhadamente, é uma composição de símbolos, caracteres com funções especiais, que, agrupados entre si e com caracteres literais, formam uma sequência, uma expressão. Essa expressão é interpretada como uma regra, que indicará sucesso se uma entrada de dados qualquer casar com essa regra, ou seja, obedecer exatamente a todas as suas condições.'''

import re # esse módulo fornece operações com expressões regulares (ER)

# lista de termos para busca
lista_pesquisa = ['informações', 'Negócios']

texto = 'Existem muitos desafios para o Big Data. O primeiro deles é a coleta dos dados, pois fala-se aqui de '\
'enormes quantidades sendo geradas em uma taxa maior do que um servidor comum seria capaz de processar e armazenar. '\
'O segundo desafio é justamente o de processar todas essas informações. Com elas então distribuídas, a aplicação deve ser '\
'capaz de consumir partes das informações e gerar pequenas quantidades de dados processados, que serão calculados em '\
'conjunto depois para criar o resultado final. Outro desafio é a exibição dos resultados, de forma que as informações '\
'estejam disponíveis de forma clara para os tomadores de decisão.'

# exemplo de data mining
for item in lista_pesquisa:
    print('Buscando por "%s" em: \n\n"%s"' % (item, texto))

     # Verificando se o termo de pesquisa existe no texto
    if re.search(item,  texto):
        print ('\n')
        print ('Palavra encontrada. \n')
    else:
        print ('\n')
        print ('Palavra não encontrada.')
        print ('\n')