'''
Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois
cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga
CPMF de 0,38% e o saldo inicial da conta está zerado.
Autor:Jules do Nascimento Pires
Ex:017
'''
# Biblioteca OS
import os

# Limpa a tela do prompt
os.system('cls')

# Entrada dos valores
salario = float(input("Salário mínimo: R$"))
cheque1 = float(input("Valor do primeiro cheque: R$"))
cheque2 = float(input("Valor do segundo cheque: R$"))

# Limpa a entrada dos valores
os.system('cls')

# Cálculo
cpmf1 = cheque1 * 0.38 / 100
cpmf2 = cheque2 * 0.38 / 100
saldo = salario - cheque1 - cheque2 - cpmf1 - cpmf2

# Resultado
print("Novo saldo: R${}".format(saldo))