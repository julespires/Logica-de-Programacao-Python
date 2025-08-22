'''
Faça um programa que receba três notas, calcule e mostre a média aritmética.
Autor:Jules do Nascimento Pires
Ex:002
Data:20/08/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
nota3 = float(input("Terçeira nota:"))

# Cálcula a média
media = (nota1 + nota2 + nota3) / 4

# Resultado
print("Média aritimética das notas:{:.2f} ".format(media))