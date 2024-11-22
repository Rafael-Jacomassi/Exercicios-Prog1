numeros = [0, -1, 4, -3, 5, -2, 0, 7]

positivos = []
negativos = []
zeros = []

for i in numeros:
    if i > 0:
        positivos.append(i)
    elif i < 0:
        negativos.append(i)
    else:
        zeros.append(i)

print(f"\nLista de números negativos: {negativos}\nLista de números positivos: {positivos}\nLista de zeros: {zeros}\n")