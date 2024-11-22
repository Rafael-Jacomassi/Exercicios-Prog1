"""
Desenvolva um programa que recebe duas palavras do usuário e informa se são iguais ou diferentes.
Informe se são iguais independentemente da capitalização (maiúsculas/minúsculas).
Entrada:
Digite a primeira palavra: Casa
Digite a segunda palavra: casa
Saída:
As palavras são iguais.
"""

palavra1 = str(input("\nDigite a primeira palavra: ")).lower()
palavra2 = str(input("\nDigite a segunda palavra: ")).lower()

if palavra1 == palavra2:
    print("\nAs palavras são iguais.")
else:
    print("\nAs palavras são diferentes.\n")