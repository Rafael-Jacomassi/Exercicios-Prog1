"""
Exercício 01 - Crie um programa que solicite ao usuário um número inteiro positivo
e, em seguida, faça uma contagem regressiva desse número até 1.

Entrada:
Digite um número inteiro positivo: 5

Saída:
5
4
3
2
1
Contagem regressiva concluída.
"""
numero_inserido = int(input("Digite um número inteiro positivo: "))

for numero in range(numero_inserido, 0, -1):
    print(numero)