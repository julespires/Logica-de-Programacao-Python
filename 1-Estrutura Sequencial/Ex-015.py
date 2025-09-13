'''
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de fábrica. Programa que receba o preço de fábrica
de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) o preço final do veículo.
Autor:Jules do Nascimento Pires
Ex:015
Data:25/08/2025
'''

# Biblioteca
import os

# Limpa a tela do prompt
os.system('cls')

# Recebe os dados do automóvel
precoFabrica = float(input("Informe o preço de fábrica:"))
percLucroDistribuidor = float(input("Informe o percentual de lucro do distribuidor:"))
percImpostos = float(input("Informe o percentual dos impostos:"))

# Realiza o cálculo
LucroDistribuidor = precoFabrica * percLucroDistribuidor / 100
valorImposto = precoFabrica * percImpostos / 100
precoFinal = precoFabrica + percLucroDistribuidor + percImpostos

# Mostra o resultado
print("Lucro do distribuídor R$:{}".format(LucroDistribuidor))
print("Impostos R$:{}".format(valorImposto))
print("Preço final R$:{}".format(precoFinal))