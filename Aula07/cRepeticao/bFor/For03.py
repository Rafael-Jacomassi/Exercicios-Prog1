"""
Crie um programa que calcula a soma dos primeiros 100 números naturais (de 1 a 100).
O programa deve exibir a soma final.
"""
soma = 0

for i in range (1, 101):
    soma += i

print(f"A soma dos 100 primeiros números naturais (de 1 a 100) é {soma}")