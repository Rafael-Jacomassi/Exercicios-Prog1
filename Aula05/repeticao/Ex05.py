"""
Exercício 05 – Crie um programa que solicita ao usuário para inserir números positivos
e calcula a média desses números, ignorando números negativos e zeros.
Calcule a média quando o usuário pressionar 0.

Entrada:
Digite um número positivo (ou 0 para sair): 5
Digite um número positivo (ou 0 para sair): 4
Digite um número positivo (ou 0 para sair): 1
Digite um número positivo (ou 0 para sair): 0

Saída:
A média dos números positivos é: 10.0


"""
contador_loops = 0
contador_numero = 0

while True:
    numero_inserido = float(input("\nDigite um número positivo (ou 0 para sair): "))

    if numero_inserido == 0:
        break

    if numero_inserido < 0: #ignorando números negativos
        continue

    contador_loops = contador_loops + 1

    contador_numero = contador_numero + numero_inserido

media = contador_numero / contador_loops

print(f"\nA média dos números positivos é: {media:.1f}\n")