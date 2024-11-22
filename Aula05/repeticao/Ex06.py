"""
Exercício 06 - Crie um programa onde o usuário deve adivinhar
um número gerado aleatoriamente entre 1 a 100. A cada tentativa,
exiba se ele deve tentar um número maior ou menor.
Quando o número for acertado, exiba o número de tentativas.
Dica: para gerar o número aleatório, utilize o seguinte código:
import random
numero_secreto = random.randint(1, 100)

Exemplo:
Digite um número: 50
Tente um número maior.
Digite um número: 80
Tente um número menor.
Digite um número: 61
Parabéns! Você acertou o número em 3 tentativas.
"""

import random
numero_secreto = random.randint(1, 100)

numero_inserido = int(input("Digite um número: "))

contador = 1

while numero_inserido != numero_secreto:
    contador = contador + 1

    if numero_inserido > numero_secreto:
        print("\nTente um número menor.")
        numero_inserido = int(input("Digite um número: "))
    elif numero_inserido < numero_secreto:
        print("\nTente um número maior.")
        numero_inserido = int(input("Digite um número: "))

if contador == 1:
    print(f"\nParabéns! Você acertou o número em 1 tentativa.\n")
else:
    print(f"\nParabéns! Você acertou o número em {contador} tentativas.\n")