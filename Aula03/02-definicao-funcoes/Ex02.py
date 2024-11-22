"""
Exercício 02 – Calcule a área de um triângulo usando uma função.

Crie uma função `calcular_area_triangulo` que receba a base e a altura como parâmetros e retorne a área do triângulo.

Entrada:
Digite a base do triângulo: 10
Digite a altura do triângulo: 5

Saída:
A área do triângulo é: 25.0

"""

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

def calcular_area_triangulo(b, a):
    resultado = (b * a) / 2
    return resultado

print(f"A área do triângulo é: {calcular_area_triangulo(base, altura)}")