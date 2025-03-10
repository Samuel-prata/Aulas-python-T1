'''     LISTAS  '''

''' 
- MUTAVEIS
- ORDENADAS
- VALORES SÃO ACESSADOS A PARTIR DE INDICES
'''

minha_lista_de_filmes = ['a procura da Felicidade', 'Escritores da liberdade', 'Jogo da imitação', 'Matrix', 'Shrek', 'Pequena sereia', 'Estrelas além do tempo', 'O menino do pijama listrada', 'A volta dos que não foram', 'As tranças do rei careca', 'As tranças do rei careca'] # Tem colchetes, isso é uma lista

print(minha_lista_de_filmes)
print('*'*100)

minha_lista_de_filmes.append('O rapto do menino dourado') # Adiciona dados como ultimo elemento da lista

print(minha_lista_de_filmes)
print('*'*100)

minha_lista_de_filmes.sort() # Ordena a lista

print(minha_lista_de_filmes)
print('*'*100)

# count() -> Conta quantas vezes o mesmo elemento aparece na lista
print(minha_lista_de_filmes.count('As tranças do rei careca'))

print(minha_lista_de_filmes)
print('*'*100)

# insert() -> Adiciona o elemento no index indicado
minha_lista_de_filmes.insert(3, 'Zacarias')
print(minha_lista_de_filmes)
print('*'*100)

print(len(minha_lista_de_filmes))
# index() -> Encontra a posição do elemento 
print(minha_lista_de_filmes.index('Escritores da liberdade'))
print(minha_lista_de_filmes)


for filme in minha_lista_de_filmes:
    print(filme)

