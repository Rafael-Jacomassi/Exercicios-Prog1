# Ex. 03: Encontrar o Menor Número em uma Lista
# Dada a lista `numeros`, use um laço `while` para encontrar o menor número na lista.

numeros = [10, 26, 87, 4, 54, 32, 77, 14, 8, 11, 11]
ja_verificados = []
tamanho_lista = len(numeros)
contador = 0
menor_numero = numeros[0]

while contador < tamanho_lista:
    if numeros[contador] not in ja_verificados:
        if numeros[contador] < menor_numero:
            menor_numero = numeros[contador]
    contador += 1

print(f"\nO menor número da lista é {menor_numero}\n")