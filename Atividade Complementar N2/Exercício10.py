'''Escreva um programa que avalia a força de cada uma com base nos seguintes critérios: 
o Força Fraca: Menos de 8 caracteres. 
o Força Média: Entre 8 e 12 caracteres, sem caracteres especiais. 
o Força Forte: Entre 8 e 12 caracteres, com pelo menos um caractere especial.'''

senhas = ["senha123", "P@ssw0rd2024", "admin"]
especiais = "!@#$%^&*()-_=+[]{;{}:'<>,.?/|`~"

for senha in senhas:
    if len(senha) < 8:
        print(f"Senha: {senha} - Força: Força Fraca")
    elif len(senha) >= 8 and len(senha) <= 12:
        tem_especial = False
        for letra in senha:
            if letra in especiais:
                tem_especial = True
        if tem_especial:
            print(f"Senha: {senha} - Força: Força Forte")
        else:
            print(f"Senha: {senha} - Força: Força Média")
    else:
        print(f"Senha: {senha} - Força: Força Forte")