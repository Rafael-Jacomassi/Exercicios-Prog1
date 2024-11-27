''' Escreva um programa em Python que receba um texto como uma string e identifique a maior 
palavra no texto. '''

texto = "Aprender Python é essencial para trabalhar com ciência de dados, automação e desenvolvimento web"
texto_limpo = texto.replace(",", "").replace(".", "")
palavras = texto_limpo.split(" ")
maior_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra

print(maior_palavra)