"""
Exercício 04 – Crie um programa que receba uma pontuação entre 0 a 60 pontos, calcule a nota entre 0 a 10.00
e exiba a nota usando duas casas decimais.

Entrada:
Digite a pontuação: 30

Saída:
A nota é: 5.00
"""

pont = float(input("Digite a pontuação: "))

def calcular_nota(p):
    resultado = p / 6
    return resultado

print(f"A nota é: {calcular_nota(pont):.2f}")