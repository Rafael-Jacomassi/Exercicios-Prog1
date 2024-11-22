#  Ex. 06: Reverter a Ordem dos Elementos sem Usar Métodos de Lista
# Use um laço `while` para reverter a ordem dos elementos na lista `numeros` sem usar o método `reverse()` ou slicing.
# A lista `numeros` deve ser modificada diretamente.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = len(numeros) - 1
reverso = []

while contador >= 0:
    reverso.append(numeros[contador])
    contador -= 1

print(f"\nLista revertida = {reverso}\n")