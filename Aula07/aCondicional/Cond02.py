"""
Faça um programa que pede dois números e mostra qual deles é o maior.
"""
numero1 = int(input("\nDigite um número: "))
numero2 = int(input("\nDigite um segundo número: "))

if numero1 > numero2:
    print(f"\n{numero1} é maior que {numero2}.\n")
elif numero1 < numero2:
    print(f"\n{numero1} é menor que {numero2}.\n")
else:
    print(f"\n{numero1} é igual a {numero2}.\n")