"""
Exercício 07 - Crie um programa que verifica a senha inserida pelo usuário, permitindo um número limitado de tentativas.
Instruções:
Definir uma senha correta (por exemplo, "1234").
Solicitar ao usuário que insira a senha.
Usar um loop while para verificar se a senha está correta, com um limite de 3 tentativas.
Informar o usuário se a senha estiver incorreta e solicitar outra tentativa.
Após o loop, verificar se a senha está correta.
Exibir "Senha correta. Acesso concedido" se a senha estiver correta.
Se o número de tentativas exceder 3, exibir "Você excedeu o número de tentativas permitidas. Acesso negado."

Exemplo:
Digite a senha: 123
Senha incorreta. Tente novamente.
Digite a senha: 234
Senha incorreta. Tente novamente.
Digite a senha: 122
Senha incorreta. Tente novamente.
Você esgotou suas tentativas. Acesso negado.
"""

senha_correta = "1234"

senha_inserida = input("\nInsira a senha: ")

contador = 0

while senha_inserida != senha_correta:
    contador = contador + 1

    if contador >= 3:
        break

    senha_inserida = input("\nA senha está incorreta, tente outra vez: ")

if contador >= 3:
    print("\nVocê esgotou suas tentativas. Acesso negado.\n")
else:
    print("\nSenha correta. Acesso concedido.\n")