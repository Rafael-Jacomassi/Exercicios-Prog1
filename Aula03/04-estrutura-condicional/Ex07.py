"""
Exercício 07 – Crie um programa que solicita ao usuário
um número inteiro e verifica se é
positivo, negativo ou zero.
Utilize a estrutura elif.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.
"""

num = int(input("Digite um número inteiro: "))

def eh_oque(x):
    if x > 0:
        return f"\n{num} é um número positivo.\n"
    elif x < 0:
        return f"\n{num} é um número negativo.\n"
    else:
        return f"\n{num} é zero.\n"
    
print(eh_oque(num))