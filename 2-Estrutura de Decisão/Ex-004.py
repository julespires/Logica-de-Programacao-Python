'''
Faça um programa que receba um número inteiro e verifique se é par ou ímpar.
Autor:Jules do Nascimento Pires
Ex-004
'''

# Biblioteca Os
import os

# Limpa a tela do prompt
os.system('cls')

num = int(input("Digite um número desejado:"))

# Limpa a entrada do número digitado
os.system('cls')

# Condições
if (num % 2 == 0):

    print("O número {} é par!".format(num))

else:
    print("O número {} é impar!".format(num))