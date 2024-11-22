"""
Exercício 06 – Desenvolva um programa que solicite
ao usuário o valor total de suas compras como um número decimal (float).
Se o valor informado for R$ 150,00 ou mais, aplique
automaticamente um desconto de 10%.
Exiba o valor total com desconto aplicado,
bem como o total economizado com o desconto.

Entrada:
Digite o valor total de suas compras: 200.00

Saída:
O valor total com desconto é R$ 180.00.
Você economizou R$ 20.00.
"""

valor_total = float(input("Digite o valor total de suas compras: "))

desconto = float(valor_total*(10 / 100))

if(valor_total >= 150):
    print(f"\nO valor total com desconto é R$ {(valor_total - desconto):.2f}\nVocê economizou R$ {desconto:.2f}.\n")
else:
    print(f"\nO valor total de suas compras é R$ {valor_total:.2f}.\n")