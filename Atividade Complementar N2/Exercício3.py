'''Escreva um programa em Python que receba uma lista de números e retorne o menor número 
presente na lista. Não utilize funções prontas como min().'''

numeros = [2, 4, 7, 6, 8, 2, 3, 5, 6, 3]
menor_numero = numeros[0]

for n in numeros:
    if n < menor_numero:
        menor_numero = n
        
print(menor_numero)