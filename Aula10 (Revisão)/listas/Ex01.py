"""
Multiplicação de Elementos
Dada uma lista de números, multiplique todos os elementos entre si e exiba o resultado.

Exemplo:
Entrada: [1, 2, 3, 4]
Saída: 24
"""
numeros =  [1, 2, 3, 4]
multi = 1

for n in numeros:
    multi *= n

print (multi)