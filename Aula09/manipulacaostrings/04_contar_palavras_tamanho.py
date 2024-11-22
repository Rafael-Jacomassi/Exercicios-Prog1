def contar_palavras_por_tamanho(frase):
    frase_limpa = frase.replace(",", "").replace(".","")
    palavras = frase_limpa.split(" ")
    for palavra in palavras:
        print(f"{palavra}: {len(palavra)}")


(contar_palavras_por_tamanho("Python é uma linguagem de programação incrível"))

#resultado esperado:
# Python: 6
# é: 1
# uma: 3
# linguagem: 9
# de: 2
# programação: 11
# incrível: 8
