"""
Exercício 08 – Crie um programa que solicita ao usuário um número de 1 a 7
e determina o dia da semana correspondente (utilizando elif).
Por exemplo, 1 representa domingo, 2 representa segunda-feira e assim por diante.

Entrada:
Digite um número de 1 a 7: 3

Saída:
3 é terça-feira.
"""
0
num = int(input("\nDigite um número de 1 a 7: "))

def que_dia(x):
    if x == 1:
        return f"\n{x} é domingo.\n"
    elif x == 2:
        return f"\n{x} é segunda-feira.\n"
    elif x == 3:
        return f"\n{x} é terça-feira.\n"
    elif x == 4:
        return f"\n{x} é quarta-feira.\n"
    elif x == 5:
        return f"\n{x} é quinta-feira.\n"
    elif x == 6:
        return f"\n{x} é sexta-feira.\n"
    elif x == 7:
        return f"\n{x} é sábado.\n"
    else:
        return "\nO número não é válido!\n"
    
dia = que_dia(num)

print(dia)