#Ex. 05: Contar Caracteres em uma Lista de Palavras
# Dada uma lista de palavras, use um laço `while` para contar o número total de caracteres em todas as palavras.
# Dica: Use a função `len()` para contar o número de caracteres em cada palavra.

palavras = ["cachorro", "gato", "prato", "paralelepípedo", "dinheiro"]
contador = 0
ja_verificados = []
tamanho_lista = len(palavras)
quantidades = []

while contador < tamanho_lista:
    quantidade = len(palavras[contador])
    ja_verificados.append(palavras[contador])
    contador += 1
    quantidades.append(quantidade)

print(f"\nQuantidade de caracteres por palavra: {quantidades}\n")