"""
Exercício 04 - Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
Entrada:
Digite um número inteiro: 5

Saída:
5 é um número positivo.

"""
num = int(input("Digite um número inteiro: "))

if(num > 0):
    print(f"\n{num} é um número positivo.\n")

if(num < 0):
    print(f"\n{num} é um número negativo.\n")

if(num == 0):
    print(f"\n{num} é zero.\n")