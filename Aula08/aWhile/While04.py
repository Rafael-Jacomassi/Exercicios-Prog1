# Ex. 04: Listar Números Pares e Ímpares
# Use um laço `while` para separar os números pares e ímpares em duas listas diferentes a partir da lista `numeros`.

# Inicializa a lista `numeros` com os números de 1 a 10.

numeros = list(range(1, 11))
tamanho_lista = len(numeros)
contador = 0
pares = []
impares = []


while contador < tamanho_lista:
    if numeros[contador] % 2 == 0:
        pares.append(numeros[contador])
    else:
        impares.append(numeros[contador])
    contador += 1

print(f"\nLista dos pares = {pares}\nLista dos ímpares = {impares}\n")