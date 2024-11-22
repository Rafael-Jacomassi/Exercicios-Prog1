"""Ex 08 - Divida uma lista com base na primeira letra de cada palavra.
Exemplo, dada a lista `animais` exiba a lista:
G
Gato
C
Cachorro
Cobra
V
Vaca
...
"""

animais = ["gato", "cachorro", "vaca", "tigre", "leão", "raposa", "tubarão", "cobra", "tartaruga", "rato", "macaco", "urso"]
animais.sort()
letra_atual = ""

for animal in animais:
    primeira_letra = animal[0].upper()
    if primeira_letra != letra_atual:
        letra_atual = primeira_letra
        print(letra_atual)
    print(animal.capitalize())