"""
Crie um programa que gere senhas aleatórias seguras para proteger
contas e sistemas. O programa deve gerar 5 senhas contendo
exatamente 8 caracteres cada.

Para garantir a segurança, cada senha deve incluir:
No mínimo:
- Uma letra maiúsculas (A-Z),
- Uma letra minúsculas (a-z),
- Um Números (0-9),
- Um Caracteres especiais (como @, #, &, etc.).
Utilize um laço para gerar as senhas e exibi-las na saída formatada.
"""

import random
import string

alfabeto_minusculas = list(string.ascii_lowercase)

alfabeto_maiusculas = list(string.ascii_uppercase)

numeros = list("0123456789")

caracteres_especiais = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~") # Lista de caracteres especiais

senha_lista = []

for n in range(5):
    senha = ""
    senha += random.choice(alfabeto_maiusculas)
    senha += random.choice(alfabeto_minusculas)
    senha += random.choice(numeros)
    senha += random.choice(caracteres_especiais)

    while len(senha) < 8:
        senha += random.choice(alfabeto_maiusculas + alfabeto_minusculas + numeros + caracteres_especiais)
    
    senha_lista = list(senha)
    random.shuffle(senha_lista)

    senha_aleatoria = ""
    for caracter in senha_lista:
        senha_aleatoria += caracter

    print(senha_aleatoria)