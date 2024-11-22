# Ex. 02: Somar os Elementos de uma Lista
# Dada a lista `numeros`, use um laço `while` para calcular a soma de todos os elementos da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tamanho_lista = len(numeros)
contador = 0
soma = 0

while contador < tamanho_lista:
    soma += numeros[contador]
    contador += 1

print(f"\nA soma de todos os elementos da lista é {soma}\n")