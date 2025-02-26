# Condicionais

email = 'samucatigrao@gmail.com'
email_digitado = input('Digite o email: ') #o que o usuario colocou
email_digitado = email_digitado.lower() 
senha = 'Samu123'
senha_digitada = input('Digite a senha: ')

# == -> igual
# !=-> diferente
# > -> maior
# >= -> maior ou igual
# < -> menor
# <= -> menor ou igual


'''OPERADORES BOOLEANOS
&& -> AND
|| -> OR
! -> NOT
'''
if senha_digitada == senha and email_digitado == email:
    print('Logado com sucesso!')

elif senha_digitada != senha:
    print('Senha incorreta')
    
else:
    print('Credenciais inválidas')
    


