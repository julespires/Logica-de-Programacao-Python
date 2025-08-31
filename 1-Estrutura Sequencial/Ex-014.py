'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
Autor:Jules do Nascimento Pires
Ex:0014
'''

# Biblioteca do sistema
import os
# Biblioteca data
from datetime import date

# Recupera o ano atual do sistema
anoAtual = date.today().year

# Limpa o terminal
os.system('cls')

# Entrada dos dados
anoNasc = int(input("Informe o ano de nascimento:"))

# Cálculo
idade = anoAtual - anoNasc
id2050 = 2050 - anoNasc

# Mostra o resultado
print("Você tem {} anos e sua idade em 2050 será {} anos".format(idade, id2050))