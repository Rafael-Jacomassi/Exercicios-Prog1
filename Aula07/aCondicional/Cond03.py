"""
Crie um programa que verifica se um número é positivo, negativo ou zero.
Utilize elif.
"""
numero = int(input("\nDigite um número: "))

if numero > 0:
    print(f"\n{numero} é um número positivo.\n")
elif numero < 0:
    print(f"\n{numero} é um número negativo.\n")
else:
    print(f"\n{numero} é 0.\n")