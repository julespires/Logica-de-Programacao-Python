'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:005
Data:20/08/2025
'''
# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
salFun = float(input("Informe o salário do funcionário: R$"))
percAumento = float(input("Informe o percentual de aumento: %"))

# Cálculo
aumento = salFun * percAumento / 100
novoSal = salFun + aumento

# Resultado
print("Valor do aumento: {}R$".format(aumento))
print("Valor do novo salário: R${}".format(novoSal))