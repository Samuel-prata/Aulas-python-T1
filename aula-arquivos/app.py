'''SISTEMA DE CADASTRO EM ARQUIVO'''

import csv # Manipulação de arquivos CSV
import time # Timer 
import os # Manipulação do sistema operacional

print('-'*50)
nome_completo = input('Digite seu nome completo: ')
print('-'*50)
data_de_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
print('-'*50)
cpf = input('Digite seu CPF (exemplo: 111.222.333-44): ')

with open('ficha_cadastro.csv', 'a') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome_completo, data_de_nascimento, cpf])
    
print()
print('**********************************')
print('* Cadastro realizado com sucesso *')
print('**********************************')
os.system('cls')

for i in range(10):
    print(f'Gerando o arquivo em {i+1}')
    time.sleep(1)
    os.system('cls')
    

with open('ficha_cadastro.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    for linha in dados:
        print(linha)