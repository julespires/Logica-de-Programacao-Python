'''
Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
a) o número digitado ao quadrado;
b) o número digitado ao cubo;
c) a raiz quadrada do número digitado;
d) a raiz cúbica do número digitado.
Autor:Jules do Nascimento Pires
Ex:011
Data:23/08/2025
'''

import math
import os

os.system('cls')

# Entrada do número
num = float(input("Digite um número:"))

# Realiza o cálculo
quadrado = pow(num, 2)
cubo = pow(num, 3)
raizquadrada = math.sqrt(num)
raizcubica = pow(num, 1/3)

# Mostra o resultado para o usuário
print("O número {} ² = {}".format(num, quadrado))
print("O número {} ³ = {}".format(num, cubo))
print("A raiz quadrade de {} = {:.2f}".format(num,raizquadrada))
print("A raiz cúbica de {} = {:.2f}".format(num,raizcubica))