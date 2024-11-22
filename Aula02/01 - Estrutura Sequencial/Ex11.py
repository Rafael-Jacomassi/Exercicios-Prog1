"""
Exercício 11 – Peça ao usuário dois números e verifique se ambos são pares,
se ambos são ímpares e se um é par e o outro ímpar.

Entrada:
Digite o primeiro número: 4
Digite o segundo número: 7

Saída:
Ambos são pares? False
Ambos são ímpares? False
Um é par e o outro ímpar? True
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número "))

rest1 = num1 % 2
rest2 = num2 % 2

msg1 = f"Ambos são pares? {rest1 == 0 and rest2 == 0}"
msg2 = f"Ambos são ímpares? {rest1 != 0 and rest2 != 0}"
msg3 = f"Um é par e o outro é impar? {(rest1 == 0 and rest2 != 0) or (rest1 !=0 and rest2 == 0) }"

print(f"\n{msg1}\n{msg2}\n{msg3}\n")