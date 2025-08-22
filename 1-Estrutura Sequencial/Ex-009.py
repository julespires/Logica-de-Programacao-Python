'''
Faça um programa que calcule e mostre a área de um triângulo. Sabe-se que: Área = (base * altura)/2.
Autor:Jules do Nascimento Pires
Ex:007
Data:21/08/2025
'''
# Biblioteca de sistema
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
base = float(input("Base:"))
altura = float(input("Altura:"))

# Cálculo da área
area = (base * altura) / 2

# Resultado
print("Área do triângulo:{}Cm".format(area))