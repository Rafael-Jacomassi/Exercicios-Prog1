'''Escreva um programa em Python que receba um texto e uma palavra. Conte quantas vezes a palavra 
aparece no texto.'''

texto = "O Python é ótimo. Eu amo Python porque Python é fácil de aprender."
texto_limpo = texto.replace(",", "").replace(".", "")
palavras = texto_limpo.split(" ")
palavra = "Python"
contador = 0

for p in palavras:
    if p == palavra:
        contador += 1
        
print(contador)