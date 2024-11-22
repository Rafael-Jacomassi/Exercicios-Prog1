lista = []

while True:
    palavra = input("Digite uma palavra (ou S para sair): ")

    if palavra.lower() == "s":
        break
    else:
        lista.append(palavra)

tamanho = len(lista)

print(f"Você digitou a lista: {lista} com tamanho {tamanho}.")