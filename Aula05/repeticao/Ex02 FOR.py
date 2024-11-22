"""
Exercício 02 - Crie um programa que solicite um número inteiro positivo e,
em seguida, imprima todos os números ímpares entre 0 e o número escolhido.
Entrada:
Digite um número inteiro positivo: 10
Saída:
1
3
5
7
9
"""
numero_inserido = int(input("Digite um número inteiro positivo: "))

for numero in range (0, numero_inserido + 1):
    if numero % 2 != 0:
        print(numero)