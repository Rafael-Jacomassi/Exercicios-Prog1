# Ex. 01: Criar e Preencher uma Lista
# Crie uma lista chamada `numeros` e use um laço `while` para adicionar os números de 1 a 10 nela.

numeros = []
n = 1

while n <= 10:
    numeros.append(n)
    n += 1

print(f"\nLista = {numeros}\n")