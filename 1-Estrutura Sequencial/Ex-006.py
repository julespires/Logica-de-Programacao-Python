'''
Programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% tam- bém sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:006
Data:20/08/2025
'''

# Biblioteca
import os

# Limpa a entrada
os.system('cls')

# Entrada de dados
salarioBase = float(input("Informe o salário base:"))

# Cálculo
gratificacao = salarioBase * 5 / 100
imposto = salarioBase * 7 / 100
salarioReceber = salarioBase + gratificacao - imposto

# Resultado
print("Novo salário a receber: R${}".format(salarioReceber))