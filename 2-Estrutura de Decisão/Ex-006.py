'''
Faça um programa que receba um número inteiro e verifique se é par ou ímpar.
Autor:Jules do Nascimento Pires
Ex:006
Data:
'''

import os

os.system('cls')

num = int(input("Digite um número:"))

if  (num % 2 == 0):
    print("O número {} é par!".format(num))

else:
    print("O número {} é impar!".format(num))