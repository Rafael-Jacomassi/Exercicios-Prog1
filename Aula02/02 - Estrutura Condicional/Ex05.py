"""
Exercício 05 - Faça um programa que recebe uma nota (0 a 10) e mostra se o aluno está reprovado (nota abaixo de 6),
de recuperação (nota entre 6 e 7) ou aprovado (nota acima de 7).

Entrada:
Digite a nota do aluno: 8

Saída:
O aluno está aprovado.

"""

nota_ = float(input("Digite a nota do aluno: "))

nota = round(nota_, 1)

if(nota < 6):
    print(f"\nO aluno está reprovado.\n")

if(nota == 6 or nota == 7):
    print(f"\nO aluno está de recuperação.\n")

if(nota > 7):
    print(f"\nO aluno está aprovado.\n")