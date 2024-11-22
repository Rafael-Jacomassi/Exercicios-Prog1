"""
Dada uma lista de números (lista_numeros = [15, 5, 10, 60 , 50, 40]),
escreva um programa que percorre a lista e exiba o menor elemento.

Obs: Não é permitido usar a função min() para encontrar o maior elemento.
"""

lista_numeros = [15, 5, 10, 60, 50, 40]

menor_numero = lista_numeros[0]

for i in lista_numeros:
    if i < menor_numero:
        menor_numero = i

print(f"\nO menor elemento da lista é: {menor_numero}\n")