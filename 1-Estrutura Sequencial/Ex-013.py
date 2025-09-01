'''
Sabe-se que:
pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
Programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.
a) polegadas;
b) jardas;
c) milhas.
Autor:Jules do Nascimento Pires
Ex:013
'''

import os

# Limpa o terminal
os.system('cls')

# Entrada da medida em pés
pes = float(input("Informe uma medida em pés:"))

# Limpa a entrada da medida
os.system('cls')

# Realiza a conversão
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

# Mostra o resultado
print("Medidas em polegadas: {}".format(polegadas))
print("Medidas em jardas:{}".format(jardas))
print("Medida em milhas:{}".format(milhas))