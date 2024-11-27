"""
Modifique o programa anterior para que,
caso o usuário já exista, seja adicionado
um número sequencial ao final do nome.

Por exemplo: joao.silva1, joao.silva2, e assim por diante.
"""

nomes_completos = [
 'Joao Silva', 'Maria Oliveira', 'Ana Santos', 'Joao Silva', 'Joao Silva',
 'Maria Oliveira', 'Carlos Souza', 'Fernanda Costa', 'Lucas Pereira',
 'Camila Almeida', 'Pedro Lima', 'Joao Silva', 'Maria Oliveira',
 'Carlos Souza', 'Fernanda Costa', 'Jose Martins', 'Rafaela Gomes',
 'Daniel Ferreira', 'Clara Rocha', 'Vinicius Mendes', 'Sofia Ramos',
 'Miguel Araujo', 'Luis Monteiro', 'Larissa Barros', 'Isabela Nogueira',
 'Matheus Moreira', 'Helena Teixeira', 'Henrique Carvalho',
 'Eduarda Figueiredo', 'Rafael Batista', 'Bruna Pinto'
]
usuarios = []

for nome_completo in nomes_completos:
    separado = nome_completo.split(" ")
    usuario_base = separado[0].lower() + "." + separado[1].lower()

    contador = 0
    for usuario in usuarios:
        if usuario == usuario_base:
            contador += 1
        else:
            if len(usuario) > len(usuario_base):
                nome_base_com_numero = usuario[:len(usuario_base)]
                if nome_base_com_numero == usuario_base:
                    numero = usuario[len(usuario_base):]
                    if numero == str(contador):
                        contador += 1

    if contador > 0:
        usuario = usuario_base + str(contador)
    else:
        usuario = usuario_base

    usuarios.append(usuario)

print(usuarios)