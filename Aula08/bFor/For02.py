# Ex. 02: Somar os Elementos de uma Lista
# Dada a lista `numeros`, use um laço `for` para calcular a soma de todos os elementos da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in numeros:
    soma += i
print(f"\nA soma de todos os elementos da lista é {soma}\n")