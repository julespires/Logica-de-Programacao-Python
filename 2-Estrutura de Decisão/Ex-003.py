'''
Faça um programa que receba dois números e mostre o maior.
Autor:Jules do Nascimento Pires
Ex:001
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Limpa a entrada de dados
os.system('cls')

# Condições
if num1 > num2:
    print("O número {} é maior!".format(num1))

if num2 > num1:
    print("O número {} é maior!".format(num2))

if num1 == num2:
    print("O valores são iguais!")