# Ex. 03: Encontrar o Menor Número em uma Lista
# Dada a lista `numeros`, use um laço `for` para encontrar o menor número na lista.

numeros = [10, 26, 87, 4, 54, 32, 77, 14, 8, 11]
menor_numero = numeros[0]

for i in numeros:
    if i < menor_numero:
        menor_numero = i

print(f"\nO menor número da lista é {menor_numero}\n")