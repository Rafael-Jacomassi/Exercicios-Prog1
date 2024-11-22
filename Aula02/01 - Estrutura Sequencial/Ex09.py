"""
Exercício 09 – Crie um programa que solicite ao usuário a entrada de um número inteiro.
O programa deve calcular e exibir os seguintes resultados:

O dobro do número.
O triplo do número.
O quadrado do número.
O cubo do número.
A metade do número.

Entrada:
Digite um número inteiro: 4

Saída:
O dobro de 4 é 8.
O triplo de 4 é 12.
O quadrado de 4 é 16.
O cubo de 4 é 64.
A metade de 4 é 2.0.

"""

num = int(input("Digite um número inteiro: "))

dobro = num * 2
triplo = num * 3
quadrado = num ** 2
cubo = num ** 3
metade = float(num / 2)

print(f"O dobro de {num} é {dobro}.\nO triplo de {num} é {triplo}.\nO quadrado de {num} é {quadrado}.\nO cubo de {num} é {cubo}.\nA metade de {num} é {metade}.")