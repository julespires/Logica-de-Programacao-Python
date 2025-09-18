'''
Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e mostre o salário a receber, seguindo estas regras:
a) a hora trabalhada vale a metade do salário mínimo.
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
c) o imposto equivale a 3% do salário bruto.
d) o salário a receber equivale ao salário bruto menos o imposto.
Autor:Jules do Nascimento Pires
Ex:016
Data:12/09/2025
'''

# Biblioteca OS
import os

# Limpa a tela do prompt
os.system('cls')

# Recebe os dados de entrada
horasTrabalhadas = float (input("Informe o número de horas trabalhadas:"))
salarioMinimo = float(input("Informe o valor do salário mínimo R$:"))

# Cálculo
valorHorasTrabalhadas = salarioMinimo / 2
valorSalarioBruto = valorHorasTrabalhadas * horasTrabalhadas
imposto = valorSalarioBruto * 3 / 100
salarioLiquido = valorSalarioBruto - imposto

# Resultado
print("Valor das horas trabalhadas: R${}".format(valorHorasTrabalhadas))
print("Valor do salário Bruto: R${}".format(valorSalarioBruto))
print("Valor do imposto: R${}".format(imposto))
print("Valor do salário líquido: R${}".format(salarioLiquido))