# Ex 06: Concatenar Strings com Separador
# Dada uma lista de palavras, use um laço `for` para concatená-las em uma única string, separadas por traços.

palavras = ["cachorro", "gato", "prato", "paralelepípedo", "dinheiro"]
concatenados = ""

for i in range(len(palavras)):
    if i == len(palavras) - 1:
        concatenados += palavras[i]
    else:
        concatenados += palavras[i] + "-"

print(f"\n{concatenados}\n")