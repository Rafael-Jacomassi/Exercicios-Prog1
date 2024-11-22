# Ex. 04: Listar Números Pares e Ímpares
# Use um laço `for` para separar os números pares e ímpares em duas listas diferentes a partir da lista `numeros`.

# Inicializa a lista `numeros` com os números de 1 a 10.
numeros = list(range(1, 11))
pares = []
impares = []


for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"\nLista de pares = {pares}\nLista de ímpares = {impares}\n")
