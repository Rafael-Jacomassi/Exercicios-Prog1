'''Escreva um programa em Python que receba uma frase e identifique todas as palavras com menos 
de 4 caracteres, exibindo-as em uma lista.'''

frase = "Python é uma linguagem poderosa e fácil de entender" 
frase_limpa = frase.replace(",", "").replace(".", "")
palavras = frase_limpa.split(" ")
palavras_mq4 = []

for palavra in palavras:
    if len(palavra) < 4:
        palavras_mq4.append(palavra)

print(palavras_mq4)