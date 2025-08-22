'''
Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = PI * R2.
Autor:Jules do Nascimento Pires
Ex:010
Data:22/08/2025
'''

# Bibliotecas utilizadas
import math
import os

# Limpa a entrada dos dados
os.system('cls')

# Entrada do raio
raio = float(input("Informe o raio do círculo:"))

# Calcula a área do círculo
area = math.pi * raio ** 2

# Mostra a área do círculo
print("A área do círculo é:{:.3f}Cm".format(area))