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
numero = int(input("Digite um número inteiro positivo: "))

contador = 0

while contador < numero:
    contador = contador + 1
    if contador % 2 != 0:
        print(contador)