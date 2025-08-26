'''
Faça um programa que apresente o menu a seguir, permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. Verifique a possibilidade de opção inválida e não se preocupe com restrições
como salário negativo.
Menu de opções:
1. Imposto
2. Novo salário
3. Classificação
Digite a opção desejada.
Na opção 1: receber o salário de um funcionário, calcular e mostrar o valor do imposto usando as regras a seguir.
SALÁRIO                                            PERCENTUAL DO IMPOSTO
Menor que R$ 500,00                                       5%
De R$ 500,00 (inclusive) a R$ 850,00 (inclusive)          10%
Acima de R$ 850,00                                        15%

Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor do novo salário, usando as regras a seguir.
SALÁRIO                                                         AUMENTO
Maior que R$ 1.500,00                                          R$ 25,00
De R$ 750,00 (inclusive) a R$ 1.500,00 (inclusive)             R$ 50,00
De R$ 450,00 (inclusive) a R$ 750,00                           R$ 75,00
Menor que R$ 450,00                                            R$ 100,00

Na opção 3: receber o salário de um funcionário e mostrar sua classificação usando a tabela a seguir.
SALÁRIO                                                       CLAssiFiCAção
Até R$ 700,00 (inclusive)                                     Mal remunerado
Maiores que R$ 700,00                                         Bem remunerado
'''

# Biblioteca 
import os

os.system('cls')

print("1. Imposto")
print("2. Novo salário")
print("3. Classificação")

op = int(input("Digite a opção desejada:"))

if op == 1:

    salario = float(input("Informe o salário do funcioniário:"))

    if salario < 500:
        imposto = salario * 5 / 100
        print("Valor do imposto: R${}".format(imposto))

    elif salario >= 500 and salario <= 850:
        imposto = salario * 10 / 100
        print("Valor do imposto: R${}".format(imposto))    

    elif salario > 850:
        imposto = salario * 15 / 100
        print("Valor do imposto: R${}".format(imposto))

if op == 2:

    salario = float(input("Informe o salário do funcionário:"))

    if salario > 1500:

        novoSal = salario + 25
        print("Seu novo salário será de: R${}".format(novoSal))
    
    elif salario > 750 and salario <= 1500:

        novoSal = salario + 50
        print("Seu novo salário será de: R${}".format(novoSal))
    
    elif salario >= 450 and salario <= 750:
        
        novoSal = salario + 75
        print("Seu novo salário será de: R${}".format(novoSal))
    
    elif salario < 450:

        novoSal = salario + 100
        print("Seu novo salário será de: R${}".format(novoSal))

if op == 3:

        salario = float(input("Informe o salário do funcionário:"))
    
if salario <= 700:
    
        print("Funcionário mal remunerado!")

else:
        print("Funcinário bem remunerado!")