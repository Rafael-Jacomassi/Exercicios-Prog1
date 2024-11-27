'''Escreva um programa em Python que receba uma lista de números e retorne o maior número 
presente na lista. Não utilize funções prontas como max().'''

numeros = [2, 4, 7, 6, 8, 2, 1, 5, 6, 3]
maior_numero = numeros[0]

for n in numeros:
    if n > maior_numero:
        maior_numero = n
        
print(maior_numero)