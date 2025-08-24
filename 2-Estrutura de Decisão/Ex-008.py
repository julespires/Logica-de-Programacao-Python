'''
Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.
Menu de opções:
1. Somar dois números.
2. Raiz quadrada de um número.
Digite a opção desejada:
'''
import math
import os

os.system("cls")

print("MENU DE OPÇÕES:")
print("1-Somar dois números.")
print("2-Raiz quadrada de um número.")

op = int(input("Digite a opção desejada:"))

if op == 1:

 num1 = int(input("Digite o primeiro valor:"))
 num2 = int(input("Digite o segundo valor:"))

 soma = num1 + num2

 print("Soma dos valores:{}".format(soma, num1, num2))

elif op == 2:
 
 num1 = int(input("Digite um número desejado:"))
 raiz = math.sqrt(num1)

 print("Raiz quadrada do número:{:.2f}".format(raiz))