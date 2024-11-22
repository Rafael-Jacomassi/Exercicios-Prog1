"""
Exercício 10 - Peça ao usuário três números e verifique se todos são iguais,
se todos são diferentes e se algum deles é maior que 50.

Entrada:
Digite o primeiro número: 25
Digite o segundo número: 50
Digite o terceiro número: 75

Saída:
Todos os números são iguais? False
Todos os números são diferentes? True
Algum número é maior que 50? True

"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

msg1 = f"Todos os números são iguais? {num1 == num2 == num3}"
msg2 = f"Todos os números são diferentes? {num1 != num2 != num3}"
msg3 = f"Algum número é maior que 50? {num1 > 50 or num2 > 50 or num3 > 50}"

print(f"\n{msg1}\n{msg2}\n{msg3}\n")