'''
Faça um programa que receba três notas de um aluno, calcule e mostre a média aritmética e a mensagem
constante na tabela a seguir. Aos alunos que ficaram para exame, calcule e mostre a nota que deverão
tirar para serem aprovados, considerando que a média exigida é 6,0.
MÉDIA ARITIMÉTICA                                              MENSAGEM
0,0 ------------- 3,0                                          Reprovado
3,0 ------------- 7,0                                          Exame
7,0 ------------- 10,0                                         Aprovado
Autor:Jules do Nascimento Pires
Ex:003
Data:23/04/2025
'''

import os

os.system('cls')

# Entrada das notas
nota1 = float(input("Primeira nota:"))
nota2 = float(input("Sgunda nota:"))
nota3 = float(input("Digite a terçeira nota:"))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

print("Média aritimética das notas:{:.2f}".format(media))

if (media >= 0) and (media < 30):

 print("Reprovado!")

if (media >= 30) and (media < 70):
  
  print("Faze exame!")

if (media >= 70) and (media <= 100):
   
   print("Aprovado!")