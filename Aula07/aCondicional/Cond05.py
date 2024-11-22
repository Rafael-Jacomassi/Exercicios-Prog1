"""
Escreva um programa que verifica se um número está dentro do
intervalo entre 10 e 20, inclusive, ou entre 30 e 40, inclusive.

Exemplo:
entrada: 10 -> "intervalo aceito."
entrada: 20 -> "intervalo aceito."
entrada: 25 -> "intervalo não aceito."
"""
numero = int(input("\nDigite um número: "))

if (numero >= 10 and numero <= 20) or (numero >= 30 and numero <= 40):
    print("\nIntervalo aceito.\n")
else:
    print("\nIntervalo não aceito.\n")