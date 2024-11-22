"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual, diferente, maior ou igual, menor ou igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
10 é diferente de 5.
10 é maior ou igual a 5.
10 não é menor ou igual a 5.

"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if(num1 > num2):
    print(f"\n{num1} é maior que {num2}.")
else:
    print(f"\n{num1} não é maior que {num2}.")

if(num1 < num2):
    print(f"{num1} é menor que {num2}.")
else:
    print(f"{num1} não é menor que {num2}.")

if(num1 == num2):
    print(f"{num1} é igual a {num2}.")
else:
    print(f"{num1} não é igual a {num2}.")

if(num1 != num2):
    print(f"{num1} é diferente de {num2}.")
else:
    print(f"{num1} não é diferente de {num2}.")

if(num1 >= num2):
    print(f"{num1} é maior ou igual a {num2}.")
else:
    print(f"{num1} não é maior ou igual a {num2}.")

if(num1 <= num2):
    print(f"{num1} é menor ou igual a {num2}.\n")
else:
    print(f"{num1} não é menor ou igual a {num2}.\n")