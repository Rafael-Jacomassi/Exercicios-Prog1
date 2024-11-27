"""
Escreva um programa que avalia a força de cada
uma com base nos seguintes critérios:

Força Fraca: Menos de 8 caracteres.
Força Média: Entre 8 e 12 caracteres, sem caracteres especiais.
Força Forte: Entre 8 e 12 caracteres, com pelo menos um caractere especial.

Exemplo de Saída:
Senha: senha123 -> Força: Média
Senha: P@ssw0rd2024 -> Força: Forte
Senha: admin -> Força: Fraca
"""

senhas = [
    "senha123", "P@ssw0rd2024", "admin", "123456", "password", "Qwerty2023!",
    "Abc12345", "SuperSecure!", "WeakPass", "Str0ng#Pass123", "abcdefgh",
    "ZxCvBnM12345", "L0ngAndComplex#", "Short1", "MyP@ssw0rd2024", "SimpleTest",
    "Test@123", "NoSpecialChar123", "Strong!CharSet$", "Minimal", "UpperCaseLOWERcase",
    "NumbersOnly123456", "Special@Only!"
]
especiais = "!@#$%^&*()-_=+[]{;{}:'<>,.?/|`~"

for senha in senhas:
    if len(senha) < 8:
        print(f"Senha: {senha} - Força: Fraca")
    elif len(senha) >= 8 and len(senha) <= 12:
        tem_especial = False
        for letra in senha:
            if letra in especiais:
                tem_especial = True
        if tem_especial:
            print(f"Senha: {senha} - Força: Forte")
        else:
            print(f"Senha: {senha} - Força: Média")
    else:
        print(f"Senha: {senha} - Força: Forte")