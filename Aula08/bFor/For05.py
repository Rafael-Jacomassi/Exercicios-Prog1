#Ex. 05: Contar Caracteres em uma Lista de Palavras
# Dada uma lista de palavras, use um laço `for` para contar o número total de caracteres em todas as palavras.
# Dica: Use a função `len()` para contar o número de caracteres em cada palavra.

palavras = ["cachorro", "gato", "prato", "paralelepípedo", "dinheiro"]
quantidades = []

for palavra in palavras:
    quantidade = len(palavra)
    quantidades.append(quantidade)

print(f"\nQuantidade de caracteres por palavra: {quantidades}\n")