"""
Crie um programa que solicita ao usuário um número entre 1 a 10.
Após isso, exiba a tabuada do número digitado.
Implemente a função imprime_tabuada que recebe um número inteiro
e imprime a tabuada desse número.
"""
n = int(input("Digite um número de 1 a 10: "))

while n not in range(1, 11):
    print("Número inválido, tente novamente!")
    n = int(input("Digite um número de 1 a 10: "))

def imprime_tabuada(n):
    multiplicador = 1
    print(f"\nTabuada do {n}:")
    while multiplicador <= 10:
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        multiplicador += 1

imprime_tabuada(n)