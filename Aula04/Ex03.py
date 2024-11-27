"""
Exercício 03 – Peça ao usuário três números inteiros
e exiba qual é o maior e qual é o menor entre eles.
Defina as funções: encontrar_maior e encontrar_menor.

Entrada:
Digite o primeiro número: 10
Digite o segundo número: 5
Digite o terceiro número: 8

Saída:
O maior número é 10.
O menor número é 5.

"""
numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("\nDigite o segundo número: "))
numero3 = int(input("\nDigite o terceiro número: "))

def encontrar_maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    else:
        if n2 > n1 and n2 > n3:
            return n2
        else:
            if n3 > n1 and n3 > n2:
                return n3

def encontrar_menor(n1, n2, n3):
    if n1 <= n2 and n1 < n3:
        return n1
    else:
        if n2 <= n1 and n2 < n3:
            return n2
        else:
            if n3 <= n1 and n3 < n2:
                return n3

# Encontrando o maior e o menor número
maior = encontrar_maior(numero1, numero2, numero3)
menor = encontrar_menor(numero1, numero2, numero3)

# Exibindo o resultado
print(f"\nO maior número é {maior}.")
print(f"\nO menor número é {menor}.\n")
