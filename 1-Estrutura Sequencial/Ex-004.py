'''
Programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:004
Data:20/08/2025
'''

# Biblioteca 
import os

# Limpa a tela
os.system('cls')

# Entrada do salário atual
salarioFuncionario = float(input("Informe o salário do funcuionário: R$"))

# Realiza os cálculos
aumento = salarioFuncionario * 25 / 100
novoSalario = salarioFuncionario + aumento

# Mostra o resultado
print("O novo salário do funcionário com 10% de aumeto é: R${}".format(novoSalario))