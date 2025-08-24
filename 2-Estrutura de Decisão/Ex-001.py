'''
A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:
NOTA                                           PESO
Trabalho de laboratório                         2
Avaliação semestral                             3
Exame final                                     5

Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela:
MÉDIA PONDERADA                                            CONCEITO
8,0 -------------- 10,0                                       A
7,0 -------------- 8,0                                        B
6,0 -------------- 7,0                                        C
5,0 -------------- 6,0                                        D
0,0 ---------------5,0                                        E
Autor:Jules do Nascimento Pires
Ex:001
Data:21/08/2025
'''

import os

os.system('cls')

notaTrab = float(input("Digite a nota do trabalho de laboratório:"))
avalSem = float(input("Digite a nota da avaliação semestral:"))
notaExame = float(input("Digite a nota do Exame final:"))

os.system('cls')

media = (notaTrab * 2 + avalSem * 3 + notaExame * 5) / 10

print("Média ponderada das notas {:.2f}".format(media))

if (media >= 8.0) and (media <= 10.0):
 
 print("Obteve conceito A!")

if (media >= 7.0) and (media < 8.0):
 
 print("Obteve conceito B!")

if (media >= 6.0) and (media < 7.0):

 print("Obteve conceito C!")

if (media >= 5.0) and (media < 6.0):

 print("Obteve Conceito D!")

if (media >= 0.0) and (media < 5.0):
 
 print("Obteve conceito E!")