'''Escreva um programa em Python que receba uma lista de números aleatórios (com possíveis 
números duplicados) e exiba apenas os números únicos, ou seja, removendo todos os duplicados. 
Não utilize funções prontas do python.'''

numeros = [1, 5, 4, 4, 3, 2, 6, 2, 4, 1, 7, 9, 9, 11, 29]
verificados = []

for n in numeros:
    if n not in verificados:
        verificados.append(n)

print(verificados)