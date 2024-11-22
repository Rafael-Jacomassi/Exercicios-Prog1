"""
Exercício 14 – Peça ao usuário dois números e verifique se o primeiro é divisível pelo segundo.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 3

Saída:
O primeiro número é divisível pelo segundo? False
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def ehDiv(n1, n2):
    resultado = n1 % n2 == 0
    return resultado

print(f"O primeiro número é divisível pelo segundo? {ehDiv(num1, num2)}")