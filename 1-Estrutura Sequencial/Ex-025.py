'''
Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo.
Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que,
pelo menos, o custo do espetáculo seja alcançado.
Autor:Jules do Nascimento Pires
Ex:025
'''

custo = float(input("Informe o custo do espetáculo:"))
convite = float(input("Informe o preço do convite:"))

custofinal = custo / convite

print("Deverá ser vendido {} convites para atingir o custo do espetáculo".format(custofinal))