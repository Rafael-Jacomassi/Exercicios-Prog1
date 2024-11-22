"""
Exercício 08 – Crie um programa que solicita dois números para o usuário,
e exibe a soma, subtração, multiplicação, divisão e resto da divisão entre eles.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
10.0 + 3.0 = 13.0
10.0 - 3.0 = 7.0
10.0 * 3.0 = 30.0
10.0 / 3.0 = 3.33
10.0 % 3.0 = 1.0
"""

num1 = float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
rest = num1 % num2

msg1 = f"{num1} + {num2} = {soma}"
msg2 = f"{num1} - {num2} = {sub}"
msg3 = f"{num1} * {num2} = {multi}"
msg4 = f"{num1} / {num2} = {div:.2f}"
msg5 = f"{num1} % {num2} = {rest}"

print(f"{msg1}\n {msg2}\n {msg3}\n {msg4}\n {msg5}")