'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:007
Data:21/08/2025
'''

# Biblioteca para limpar a entrada de dados
import os

# Limpa a tela
os.system('cls')

# Entrada do salário base
salBase = float(input("Informe o salário base do funcionário:"))

# Cálculo 
imposto = salBase * 10 / 100
salarioReceber = salBase + 50 - imposto

# Mostra o novo salário
print("Seu novo salário a receber é de R${}".format(salarioReceber))