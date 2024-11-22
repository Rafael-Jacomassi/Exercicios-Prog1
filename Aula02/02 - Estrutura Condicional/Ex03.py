"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print(f"\nO maior número é {max(num1, num2, num3)}\nO menor número é {min(num1, num2, num3)}\n")