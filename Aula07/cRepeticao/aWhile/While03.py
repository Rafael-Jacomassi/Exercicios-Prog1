"""
Crie um programa que calcula a soma dos primeiros 100 números naturais (de 1 a 100).
O programa deve exibir a soma final.
"""
soma = 0
contador = 1

while contador <= 100:
    soma += contador
    contador += 1
print(f"\nA soma dos 100 números naturais (de 1 a 100) é {soma}\n")