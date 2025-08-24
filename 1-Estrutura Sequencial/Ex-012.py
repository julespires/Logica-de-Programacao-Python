'''
Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
Autor:Jules do Nascimento Pires
Ex:012
Data:23/08/2025
'''

# Biblioteca OS
import os

# Limpa o terminal
os.system('cls')

# Entrada dos valores
num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

# Limpa a entrada dos valores
os.system('cls')

# Calcúla a raiz quadrada entre os números
quad1 = pow(num1, num2)
quad2 = pow(num2, num1)

# Mostra o resultado dos cálculos
print("-" * 30)
print("{} ao quadrado de {} = {} ".format(num1, num2, quad1))
print("{} ao quadrado de {} = {}".format(num2, num1, quad2))
print("-" * 30)