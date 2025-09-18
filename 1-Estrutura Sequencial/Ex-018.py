'''
Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a
quantidade de ração em gramas. A quantidade diária de ração fornecida para cada gato é sempre a
mesma. Faça um programa que receba o peso do saco de ração e a quantidade de ração fornecida para
cada gato, calcule e mostre quanto restará de ração no saco após cinco dias.
Autor:Jules do Nascimento Pires
Ex:018
Data:18/09/2025
'''

# Entrada dos dados
pesoSaco = float(input("Peso do saco de ração:"))
racaoGato1 = float(input("Quantidade ração gato 1:"))
racaoGato2 = float(input("Quantidade ração gato 2:"))

# Cálculo
racaoGato1 = racaoGato1 / 100
racaoGato2 = racaoGato2 / 100
totalFinal = pesoSaco - 5 * (racaoGato1 + racaoGato2)

# Mostra o resultado final
print("Total final:{}kl".format(totalFinal))
