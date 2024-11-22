"""
Exercício 04 - Escreva um programa que leia uma temperatura em graus Celsius e a converta para Fahrenheit.
A fórmula de conversão é F = C * 9/5 + 32.

Exemplo de Entrada:
Digite uma temperatura em Celsius para conversão: 25

Exemplo de Saída:
25°C é equivalente a 77.0°F
"""

C = float(input("Digite uma temperatura em Celsius para conversão: "))

F = C * 9/5 + 32

msg = f"{C}°C é equivalente a {F}°F"

print(msg)
