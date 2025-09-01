'''
Programa que receba quatro números inteiros, calcule e mostre a soma desses números.
Autor:Jules do Nascimento Pires
Ex:001
Data:20/08/2025
'''

# Biblioteca 
import os

os.system('cls')

# Entrada dos valores
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))
num3 = int(input("Terçeiro valor:"))
num4 = int(input("Quarto valor:"))

# Realiza a soma
soma = num1 + num2 + num3 + num4

# Mostra o resultado
print("Soma dos valores fornecidos: {}".format(soma, num1, num2, num3, num4))