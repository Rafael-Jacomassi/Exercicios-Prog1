"""
Ocorrências de um número:
Crie um programa que percorre a lista_numeros
e exiba quantas vezes cada número aparece na lista.
"""
lista = [5,1,2,3,3,4,3,2,5]

# comece aqui:

contados = []
print("")

for numero in lista:
    if numero not in contados:
        contador = 0
        for i in lista:
            if i == numero:
                contador += 1
        if contador == 1:
            print(f"O número {numero} aparece {contador} vez na lista.\n")
        else:
            print(f"O número {numero} aparece {contador} vezes na lista.\n")
        contados.append(numero)