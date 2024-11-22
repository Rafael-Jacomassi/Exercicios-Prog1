"""
Exercício 01 – Peça ao usuário dois números e verifique se ambos são pares, se ambos são ímpares e se um é par e o outro ímpar.
Defina uma função chamada ehPar.

"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número "))

def ehPar (num):
    resultado = num % 2 == 0
    return resultado

def ehImpar(num):
    resultado = num % 2 != 0
    return resultado

msg1 = f"Ambos são pares? {ehPar(num1) and ehPar(num2)}"
msg2 = f"Ambos são ímpares? {ehImpar(num1) and ehImpar(num2)}"
msg3 = f"Um é par e o outro é impar? {(ehPar(num1) and ehImpar(num2)) or (ehPar(num2) and ehImpar(num1)) }"

print(f"\n{msg1}\n{msg2}\n{msg3}\n")