"""
Escreva um programa que aplica descontos em compras:
-5% para compras até R$100,
-10% para compras acima de R$100 até R$500, e
-15% para compras acima de R$500.

Exiba o valor original, o valor do desconto e o valor final.
"""
valor_compra = float(input("Digite o valor da compra: "))

def calcular_desconto(x, y):
    return x * y

if valor_compra <= 100:
    print(f"\nValor Original: R${valor_compra:.2f}\nValor do desconto: R${calcular_desconto(valor_compra, 0.05):.2f}\nValor final: R${valor_compra - calcular_desconto(valor_compra, 0.05):.2f}\n")
elif valor_compra > 100 and valor_compra <= 500:
    print(f"\nValor Original: R${valor_compra:.2f}\nValor do desconto: R${calcular_desconto(valor_compra, 0.1):.2f}\nValor final: R${valor_compra - calcular_desconto(valor_compra, 0.1):.2f}\n")
else:
    print(f"\nValor Original: R${valor_compra:.2f}\nValor do desconto: R${calcular_desconto(valor_compra, 0.15):.2f}\nValor final: R${valor_compra - calcular_desconto(valor_compra, 0.15):.2f}\n")