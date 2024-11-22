texto = """
Na programação de computadores, uma string é simplesmente uma sequência de caracteres. 
Frequentemente, as strings são usadas para representar palavras ou frases, 
mas elas também podem representar qualquer sequência de caracteres, incluindo números e símbolos. 
Manipular strings é uma habilidade essencial para qualquer programador.
"""
print(texto)

# Ex 1. Calcule e imprima o número de palavras no texto.
texto_limpo = texto.replace(",", "").replace(".", "").replace("\n", "")
palavras = texto_limpo.split(" ")
print(f"Ex 1: Número de Palavras: {len(palavras)}")


# Ex 2. Encontre e imprima a palavra mais longa no texto.
palavra_maior = ""
for palavra in palavras:
    if len(palavra) > len(palavra_maior):
        palavra_maior = palavra
print(f"\nEx 2: Palavra Mais Longa: {palavra_maior}")


# Ex 3. Inverta a ordem das palavras no texto e imprima o resultado. Use 02-for ou 01-while.
# Exemplo: "Olá, mundo!" -> "mundo! Olá,"
palavras3 = texto.split(" ")
contador3 = len(palavras3) - 1
texto_invertido3 = ""
while contador3 >= 0:
    texto_invertido3 += palavras3[contador3] + " "
    contador3 -= 1
print(f"\nEx 3: Invertendo a Ordem das Palavras: {texto_invertido3}")


# Ex 4. Inverta a ordem dos caracteres no texto e imprima o resultado. Use 01-while.
# Exemplo: "Olá, mundo!" -> "!odnum ,álO"
contador4 = len(texto) - 1
texto_invertido4 = ""
while contador4 >= 0:
    texto_invertido4 += texto[contador4]
    contador4 -= 1
print(f"\nEx 4: Invertendo a Ordem dos Caracteres: {texto_invertido4}")


# Ex 5. Use um laço 02-for para listar todas as palavras no texto que começam com uma letra maiúscula.
# Utilize a função `isupper()`.
maiusculas = []
for palavra in palavras:
    if palavra[0].isupper():
        maiusculas.append(palavra)
print(f"\nEx 5: Palavras que Começam com Letra Maiúscula: {maiusculas}")

# Ex 6. Use um laço 02-for para encontrar e imprimir a primeira palavra no texto com mais de 10 letras.
palavra_10 = ""
for palavra in palavras:
    if len(palavra) >= 10:
        palavra_10 += palavra
        break
print(f"\nEx 6: Primeira Palavra com Mais de 10 Letras: {palavra_10}")


# Ex 7. Utilize um laço 01-while para contar quantas vezes a vírgula aparece no texto.
contador7 = 0
virgulas = 0
while contador7 < len(texto):
    if texto[contador7] == ",":
        virgulas += 1
    contador7 += 1
print(f"\nEx 7: Contagem de Vírgulas: {virgulas}")


# Ex 8. Utilize um laço 02-for para contar quantas vezes cada vogal (a, e, i, o, u) aparece no texto.
vogais = "aeiouãéíó"
contador_vogais = 0
for letra in texto:
    if letra in vogais:
        contador_vogais += 1
print(f"\nEx 8: Contagem de Vogais: {contador_vogais}")


# Ex 9. Encontrar e Contar Palavras que Terminam com 's'
palavras_s = []
for palavra in palavras:
    if palavra[-1] == "s":
        palavras_s.append(palavra)
print(f"\nEx 9: Palavras que Terminam com 's': {palavras_s} {len(palavras_s)} palavras.")


# Ex 10. Encontrar e Contar Palavras que Contêm 'a'
palavras_a = []
for palavra in palavras:
    if "a" in palavra or "ã" in palavra or "á" in palavra:
        palavras_a.append(palavra)
print(f"\nEx 10: Palavras que Contêm 'a': {palavras_a} {len(palavras_a)} palavras.")


# Ex 11. Contar o Número de Sentenças no Texto
contador11 = 0
for letra in texto:
    if letra  == ".":
        contador11 += 1
print(f"\nEx 11: Contagem de Sentenças: {contador11}")


# Ex 12. Reverter a Ordem das Sentenças no Texto
# Utilize um laço 01-while para inverter a ordem das sentenças no texto.
# Considere uma sentença como qualquer sequência de caracteres terminada por um ponto.
sentenças = texto.split(".")
contador12 = len(sentenças) - 1
sentenças_invertidas = ""
while contador12 >= 0:
    sentenças_invertidas += sentenças[contador12] + "."
    contador12 -= 1
print(f"\nEx 12: Invertendo a Ordem das Sentenças: {sentenças_invertidas}")


# Ex 13. Identificar e Contar Palavras Que Começam e Terminam Com a Mesma Letra
# Use um laço 02-for para identificar e contar quantas palavras no texto começam e terminam com a mesma letra.
palavras13 = []
for palavra in palavras:
    if palavra.lower()[0] == palavra.lower()[-1]:
        palavras13.append(palavra)
print(f"\nEx 13: Palavras que Começam e Terminam com a Mesma Letra: {palavras13} {len(palavras13)} palavras.")

# Ex 14. Exibir todas as palavras maiores com mais de 2 caracteres. Imprimir a palavra somente uma vez.
palavras_mais2 = []
for palavra in palavras:
    if palavra not in palavras_mais2:
        if len(palavra) > 2:
            palavras_mais2.append(palavra)
print(f"\nEx 14: Palavras com Mais de 2 Caracteres: {palavras_mais2}")