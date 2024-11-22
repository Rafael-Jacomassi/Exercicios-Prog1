"""
Exercício 02: Calculadora de Fatorial
Peça ao usuário um número inteiro positivo e calcule o fatorial desse número usando while.

Entrada: 4
Saída: 24 (4! = 4 * 3 * 2 * 1
Entrada: 5
Saída: 120 (5! = 5 * 4 * 3 * 2 * 1)
"""
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1
listinha = ""
multiplicador = n

while multiplicador >= 1:
    fatorial *= multiplicador
    if multiplicador > 1:
        listinha += f" {multiplicador} *"
    else:
        listinha += f" {multiplicador})"
    multiplicador -= 1

print(f"{fatorial} ({n}! ={listinha}")