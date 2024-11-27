'''Escreva um programa em Python que receba um texto como uma string, transforme-o em uma lista 
de palavras e conte quantas palavras o texto possui. 
Use como entrada: texto = "Python é uma linguagem de programação poderosa e versátil."'''

texto = "Python é uma linguagem de programação poderosa e versátil."

texto_limpo = texto.replace(",", "").replace(".", "")
palavras = texto_limpo.split(" ")

print(len(palavras), "palavras")