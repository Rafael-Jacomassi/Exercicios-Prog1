"""
Faça um programa que recebe uma nota (0 a 10) e mostra se o aluno está reprovado (nota abaixo de 6),
de recuperação (nota entre 6 e 7) ou aprovado (nota acima de 7).
"""
nota = float(input("\nDigite uma nota entre 0 a 10: "))

if nota < 6:
    print("\nO aluno está reprovado.\n")
elif nota >= 6 and nota <= 7:
    print("\nO aluno está de recuperação.\n")
elif nota > 7 and nota <= 10:
    print("\nO aluno está aprovado.\n")
else:
    print("\nA nota está fora do intervalo.\n")