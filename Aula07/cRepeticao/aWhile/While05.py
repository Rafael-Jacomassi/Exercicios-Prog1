"""
Adivinhe o Número
Implemente um jogo simples onde o programa escolhe aleatoriamente um número entre 1 e 100,
e o usuário tenta adivinhar esse número.
Após cada tentativa, o programa informa se o palpite está correto,
é muito alto, ou muito baixo, continuando até o usuário acertar.
"""
import random

numero_secreto = random.randint(1, 100)
numero_inserido = int(input("Digite um número: "))

while numero_inserido != numero_secreto:
    if numero_inserido > numero_secreto:
        numero_inserido = int(input("O palpite está muito alto: "))
    else:
        numero_inserido = int(input("O palpite está muito baixo: "))

print("\nO palpite está correto!\n")