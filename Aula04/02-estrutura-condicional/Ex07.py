"""
Exercício 07 - Escreva um programa que recebe o valor total
e aplica descontos em compras:
-5% para compras até R$100,
-10% para compras acima de R$100 até R$500, e
-15% para compras acima de R$500.
Exiba o valor original, o valor do desconto e o valor final.

Entrada:
Digite o valor total das suas compras (em R$): 200

Saída:
Valor total: R$ 200.00
Valor com desconto: R$ 180.00
Desconto: R$ 20.00
"""
valor_total = float(input("Digite o valor total das suas compras (em R$): "))

def calcular_desconto(x, y):
    resultado = float(x * (y / 100))
    return resultado

if (valor_total >= 0 and valor_total <= 100):
    print(f"\nValor total: R$ {valor_total:.2f}\nValor com desconto: R$ {valor_total - calcular_desconto(valor_total, 5):.2f}\nDesconto: R$ {calcular_desconto(valor_total, 5):.2f}\n")
elif (valor_total > 100 and valor_total <= 500):
    print(f"\nValor total: R$ {valor_total:.2f}\nValor com desconto: R$ {valor_total - calcular_desconto(valor_total, 10):.2f}\nDesconto: R$ {calcular_desconto(valor_total, 10):.2f}\n")
elif (valor_total > 500):
    print(f"\nValor total: R$ {valor_total:.2f}\nValor com desconto: R$ {valor_total - calcular_desconto(valor_total, 15):.2f}\nDesconto: R$ {calcular_desconto(valor_total, 15):.2f}\n")
else:
    print(f"O valor total das suas compras não é valido, tente novamente!")