'''
Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar subindo a escada, calcule e mostre quantos degraus ele deverá subir para
atingir seu objetivo, sem se preocupar com a altura do usuário. Todas as medidas fornecidas devem estar em metros.
Autor:Jules do Nascimento Pires
Ex:019
Data:18/09/2025
'''

# Recebe os dados do usuário
alturaDegrau = float(input("Informa a altura do degrau:"))
alturaUsuario = float(input("Altura que deseja alcançar:"))

# Calcula a quantidade de degraus
quantidadeDegrau = alturaUsuario / alturaDegrau

# Mostra o resultado
print("Quantidade de degraus a subir:{}".format(quantidadeDegrau))