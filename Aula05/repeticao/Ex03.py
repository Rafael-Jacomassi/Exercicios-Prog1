"""
Exercício 03 – Crie um programa que calcula a soma de
números inseridos pelo usuário até que o usuário decida parar.

Entrada:
Digite um número (ou 0 para sair): 5.5
Digite um número (ou 0 para sair): 3
Digite um número (ou 0 para sair): 0

Saída:
A soma total é: 8.5
"""
contador = 0

while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    contador = contador + numero
    
    if numero == 0:
        break

print(f"A soma total é: {contador}")