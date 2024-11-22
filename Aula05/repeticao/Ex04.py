"""
Exercício 04 – Crie um programa que solicita ao usuário
para inserir uma série de números, e ele só irá somar
os números pares fornecidos. Use o comando continue.

Entrada:
Digite um número (ou 0 para sair): 5
Digite um número (ou 0 para sair): 4
Digite um número (ou 0 para sair): 1
Apenas números pares são somados. Tente novamente.
Digite um número (ou 0 para sair): 0

Saída:
A soma total dos números pares é: 4
"""

'''contador = 0
numero = int(input("Digite um número (ou 0 para sair): "))

while numero != 0:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero % 2 == 0:
        contador = contador + numero
    else:
        print("Apenas números pares são somados. Tente novamente.")

print(f"A soma total dos números pares é: {contador}")'''

#VERSÃO MELHORADA

contador = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break

    if numero % 2 == 0:
        contador = contador + numero
        continue #continue ignora oque tem embaixo dele, e volta pro começo do loop.
    else:
        print("Apenas números pares são somados. Tente novamente.")

print(f"A soma total dos números pares é: {contador}")