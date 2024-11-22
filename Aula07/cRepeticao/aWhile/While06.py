"""
Crie um programa que pede ao usuário para digitar números positivos e soma esses números.
O loop termina quando o usuário digita o número 0, e o programa exibe a soma final.

Entrada:
Digite um número: 5
Digite um número: 3
Digite um número: 2
Digite um número: 0

Saída:
A soma dos números é 10
"""
soma = 0

while True:
    n = int(input("Digite um número positivo (ou 0 para sair)): "))
    if n == 0:
        break
    elif n < 0:
        print("O número é inválido, apenas números positivos!\n")
    else:
        soma += n
    
print(f"\nA soma final é {soma}\n")