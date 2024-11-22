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
contador = 0
letra_atual = ""

while contador < len(animais):
    primeira_letra = animais[contador][0].upper()
    if primeira_letra != letra_atual:
        letra_atual = primeira_letra
        print(letra_atual)
    print(animais[contador].capitalize())
    contador += 1