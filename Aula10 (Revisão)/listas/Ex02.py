"""
Contagem de Elementos Únicos
Receba uma lista e conte quantos elementos únicos ela contém.

Entrada: [1, 2, 2, 3, 4, 4, 5]
Saída: 5
"""
elementos = [1, 2, 2, 3, 4, 4, 5]
verificados = []

for n in elementos:
    if n not in verificados:
        verificados.append(n)

print(len(verificados))