"""
Crie 10 senhas aleatórias de 6 caracteres alfanuméricos.
Exemplo de saída:
1: kvjif2
2: l0gdlk
3: 610rdh
4: 9h068a
5: 93j3pm
6: 541qo7
7: chvuzi
8: mmhlb1
9: vspqmq
10: 6l9dg6
"""
import random
caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
contador = 1

for contador in range (10):
    senha = ""
    contador += 1
    for i in range (6):
        letra_aleatoria = random.choice(caracteres)
        senha += letra_aleatoria
    print(f"{contador}: {senha}")