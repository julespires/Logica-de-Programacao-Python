'''
Programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.
Autor:Jules do Nascimento Pires
Ex:003
Data:20/08/2025
'''

# Biblioteca
import os

# limpa a tela
os.system('cls')

# Entrada de dados
nota1 = float(input('Primeira nota:'))
peso1 = int(input("Primeiro peso:"))
nota2 = float(input("Segunda nota:"))
peso2 = int(input("Segundo peso:"))
nota3 = float(input("Terçeira nota:"))
peso3 = int(input("Terçeiro peso:"))

# Limpa a entrada de dados
os.system('cls')

# Calcula a média ponderada
media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Resultado
print("Média ponderada das notas {:.2f}".format(media))