"""
Exercício 9: Armazene o maior número
Peça ao usuário para inserir números ou zero para sair.
Depois, mostre o maior número inserido.

Entrada:
Digite um número: 5
Digite um número: 3
Digite um número: 8
Digite um número: 2
Digite um número: 0

Saída:
O maior número é 8
"""
maior_numero = int(input("Digite um número (ou  para sair): "))

if maior_numero != 0:
    while True:
        n = int(input("Digite um número (ou  para sair): "))
        
        if n == 0:
            break
        elif n > maior_numero:
            maior_numero = n

print(f"O maior número é {maior_numero}")