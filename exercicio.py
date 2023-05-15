"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Informe um número inteiro: ')

if (numero.isnumeric()):
    if (int(numero)%2 == 0):
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
else:
    print(f'{numero} não é um inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 1111
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? ')
hora_sem_minutos = int(hora[0:2])

print(hora_sem_minutos)

if (hora_sem_minutos <= 11):
    print('Bom dia')
elif (hora_sem_minutos >=12 and hora_sem_minutos <=17):
    print('Boa tarde')
else:
    print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome  = input('Informe seu nome: ')
tamanho_nome = len(nome)

if(tamanho_nome <= 4):
    print('Seu nome é curto')
elif (tamanho_nome >= 5 and tamanho_nome <=6):
    print('Seu nome é normal')
else:
    print('Seu nome é muito longo')