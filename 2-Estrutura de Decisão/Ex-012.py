'''
Faça um programa que receba o código correspondente ao cargo de um funcionário e seu salário atual e mostre o cargo, o valor do aumento e seu novo salário. Os cargos estão na tabela a seguir.
Autor:Jules do Nascimento Pires
Ex:012
Data:24/08/2025
'''
# Biblioteca para limpar a entrada
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
cargo = int(input("Digite o cargo do funcionário: 1 - 2- 3 - 4 ou 5:"))
salario = float(input("Digite o valor do salário:R$"))

# Condições
if cargo == 1:

    print("Cargo escriturário:")
    aumento = salario * 50 / 100
    novoSal = salario + aumento
    print("Valor do aumento: R${}".format(aumento))
    print("Valor do novo salário:R${}".format(novoSal))

if cargo == 2:

    print('Cargo Secretário:')
    aumento = salario * 35 / 100
    novoSal = salario + aumento
    print("Valor do aumento: R${}".format(aumento))
    print("Valor do novo salário:R${}".format(novoSal))

if cargo == 3:

    print("Cargo Caixa:")
    aumento = salario * 20 / 100
    novoSal = salario + aumento
    print("Valor do aumento: R${}".format(aumento))
    print("Valor do novo salário:R${}".format(novoSal))

if cargo == 4:

    print("Cargo Gerente:")
    aumento = salario * 10 / 100
    novoSal = salario + aumento
    print("Valor do aumento: R${}".format(aumento))
    print("Valor do novo salário:R${}".format(novoSal))

if cargo == 5:

    print("Cargo Diretor, não tem aumento")    

if cargo >= 6:

    print("Opção inválida, digite o código correto!")