"""
Exercício 03 - Modifique o exercício anterior adicionando o cálculo da margem do lucro em %.
Exiba o valor com duas casas decimais.

Entrada:
Digite o preço de venda: 100
Digite o custo do produto: 80

Saída:
O lucro é de: 20.00
A margem de lucro é de: 20.00%

"""

preco = float(input("Digite o preço de venda: "))
custo = float(input("Digite o custo de venda: "))

lucro = preco - custo

margem = (lucro / preco)

print(f"O lucro é de: {lucro:.2f}\nA margem de lucro é de: {margem:.2%}")