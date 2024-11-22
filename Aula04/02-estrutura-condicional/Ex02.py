"""
Exercício 02 – Peça ao usuário dois números inteiros e exiba as comparações:
maior, menor, igual.

Crie as funções: eh_menor, eh_igual.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5

Saída:
10 é maior que 5.
10 não é menor que 5.
10 não é igual a 5.
"""
def eh_maior(a, b):
    return a > b

def eh_menor(n1, n2):
    return n1 < n2

def eh_igual(x, y):
    return x == y

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if eh_maior(numero1, numero2):
    print(f"\n{numero1} é maior que {numero2}.")
else:
    print(f"\n{numero1} não é maior que {numero2}.")

if eh_menor(numero1, numero2):
    print(f"\n{numero1} é menor que {numero2}.")
else:
    print(f"\n{numero1} não é menor que {numero2}.")

if eh_igual(numero1, numero2):
    print(f"\n{numero1} é igual a {numero2}.")
else:
    print(f"\n{numero1} não é igual a {numero2}.")