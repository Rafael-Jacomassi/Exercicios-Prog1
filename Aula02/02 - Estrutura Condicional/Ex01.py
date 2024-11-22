"""
Exercício 01 – Crie um programa que solicita um número inteiro para o usuário.
Após isso, verifique se o número é par ou ímpar.

Entrada:
Digite um número inteiro: 5

Saída:
5 é um número ímpar.

"""
num = int(input("Digite um número inteiro: "))

def eh_par(n):
    resultado = n % 2 == 0 #Isso ja retorna um True.
    return resultado

if(eh_par(num)):
    print(f"\n{num} é um número par.\n")
else:
    print(f"\n{num} é um número ímpar.\n")