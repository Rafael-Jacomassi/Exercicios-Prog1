"""
Dada uma lista de números (lista_numeros = [15, 5, 10, 60 , 50, 40]),
escreva um programa que percorre a lista e exiba o maior elemento.

Obs: Não é permitido usar a função max() para encontrar o maior elemento.
"""

lista_numeros = [15, 5, 10, 60, 50, 40]

maior_numero = lista_numeros[0]

for i in lista_numeros:
    if i > maior_numero:
        maior_numero = i

print(f"\nO maior elemento da lista é: {maior_numero}\n")