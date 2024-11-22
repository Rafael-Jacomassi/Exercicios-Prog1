"""
Crie um programa que pede ao usuário para digitar números positivos e soma esses números.
O loop termina quando o usuário digita o número 0, e o programa exibe a soma final.
"""
soma = 0
lista = []

while True:
    n = int(input("Digite um número positivo (ou 0 para sair): "))
    if n == 0:
        break
    elif n < 0:
        print("\nNúmero inválido, apenas números positivos!")
    else:
        lista.append(n)

for i in lista:
    soma += i

print(f"\nA soma dos números é igual a {soma}\n")