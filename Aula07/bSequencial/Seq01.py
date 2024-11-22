"""
Crie um programa que calcula a área de um retângulo.
O usuário deve fornecer a largura e a altura do retângulo.
Entrada:
Digite a largura do retângulo: 10
Digite a altura do retângulo: 5
Saída:
A área do retângulo é 50.00 m².
"""

largura = float(input("\nDigite a largura do retângulo: "))
altura = float(input("\nDigite a altura do retângulo: "))

area = largura * altura

print(f"\nA área do retângulo é {area:.2f} m².\n")