'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa;
b) quantos anos ela terá em 2050.
Autor:Jules do Nascimento Pires
Ex:014
'''

# Bibliotecas
import os
from datetime import datetime

# Recebe a data de nascimento pelo usuário
anoNascimento = int(input("Informe o ano de nascimento:"))

# Limpa a entrada
os.system('cls')

# Recupera o ano atual do sistema
agora = datetime.now()

# Cálculo
idade = ano_atual = agora.year - anoNascimento
idade2050 = 2050 - anoNascimento

# Mostra o resultado
print("Sua idade atual é {} anos!".format(idade))
print("Sua idade em 2050 será {} anos!".format(idade2050))
