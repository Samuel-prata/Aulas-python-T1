''' FUNÇÕES '''

'''ESTRUTURA DEFINIDA QUE PODE TRAZER UM RETORNO OU EXECUTAR UMA AÇÃO'''

'''
Funções em parametros e sem retorno
Funções com parametros e com retorno
funções com parametros e sem retorno
funções sem parametros e com retorno
'''


'''FUNÇÃO SEM PARAMETROS E SEM RETORNO'''
def somar_dois_numeros(): 
    numero1 = 10
    numero2 = 20.5
    
    print(numero1+numero2) 

somar_dois_numeros()

print('-'*100)

'''FUNÇÃO COM PARAMETROS E SEM RETORNO'''
def somar_dois_numeros(numero1: int, numero2: int):
    print(numero1 + numero2)

somar_dois_numeros(10, 10)

print('-'*100)

'''FUNÇÃO COM PARAMETROS E RETORNOS'''
def multiplicar_dois_numeros(numero1, numero2):
    return numero1*numero2

resultado_da_multiplicacao = multiplicar_dois_numeros(10, 0)
print(resultado_da_multiplicacao)


'''FUNÇÃO SEM PARAMETRO E COM RETORNO'''
def retornar():
    numero1 = 10
    numero2 = 20
    
    return numero1, numero2

retorno_da_funcao = retornar()
print(retorno_da_funcao)

print('-'*100)

# *args -> Recebe uma tupla como argumento
# Essa função recebe varios argumentos
def somar(*numeros):
    print(type(numeros))
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

resultado_da_soma = somar(1,2,3,4,5,6,7,8,10,20)
print(resultado_da_soma)
