''' DICIONARIOS '''

'''
- Mutável
- Desordenados
- chave: valor
'''

''' 
A CHAVE É UNICA: Os valores podem ser de qualquer tipo
'''

dados_pessoais = {
    'nome_completo': 'Lucas Gomes', 
    'cpf': '000.111.000-11', 
    'email': 'lucasreidopython@email.com', 
    'numero_da_casa_do_lucas': 298
    }

print(type(dados_pessoais))

print('-'*100)

# keys() -> Retornar as chaves presentes no dicionario
print(dados_pessoais.keys())

# values() -> Retornar os valores presentes no dicionario
print(dados_pessoais.values())

print('-'*100)

# print(dados_pessoais['nome'])

dados_pessoais['nome_complet'] = 'Samuel Silvério'

print(f'O nome completo passou a ser: {dados_pessoais['nome_completo']}')

print(dados_pessoais.get('nome'))

print('-'*100)

print(dados_pessoais)

print('-'*100)

# Exclusão de uma chave a partir da palavra reservada del
# del dados_pessoais['nome_complet']
dados_pessoais2 = {
    'Nome_completo': 'Felipe Zardo', 
    'CPF': '090.398.284-60', 
    'email': 'felipe@gmail.com', 
    'numero_da_casa': 290
}

print('-'*100)
print('Antes do update')
print(dados_pessoais)

# update() -> Se tiver chaves iguais, ele sobrepõe. Chaves diferentes são adicionadas
dados_pessoais.update(dados_pessoais2)
print('-'*100)
print('depois do update')
print(dados_pessoais)