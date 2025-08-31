'''
Programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.
Autor:Jules do Nascimento Pires
Ex:006
Data:21/08/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
deposito = float(input("Valor do deposito: R$"))
taxaJuros = float(input("Valor da taxa de juros:"))

# Cálculo
rendimento = deposito * taxaJuros / 100
valorTotal = deposito + rendimento

# Resultado
print("Valor do rendimento: R${}".format(rendimento))
print("Valor total: R${}".format(valorTotal))