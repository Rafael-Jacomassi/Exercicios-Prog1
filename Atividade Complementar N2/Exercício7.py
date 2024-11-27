'''Escreva um programa em Python que receba um texto como uma string e identifique a palavra mais 
curta no texto.'''

texto = "Python possui uma sintaxe clara e fácil de compreender" 
texto_limpo = texto.replace(",", "").replace(".", "")
palavras = texto_limpo.split(" ")
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print(menor_palavra)