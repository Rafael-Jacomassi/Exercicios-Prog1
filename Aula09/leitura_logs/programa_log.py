import os
pasta = os.getcwd().replace("\\", "/")

caminho_arquivo = r"C:\Users\Roberto\Documents\Fatec\Prog\Exercícios Aula 2 a 9\progI-2024-main\Aula09\leitura_logs\server.log"
print(caminho_arquivo)
arquivo = open(caminho_arquivo, "r")

#menu
while True:
    print("-"*40)
    print("Menu de opções:")
    print("1 - Exibir todas as linhas")
    print("2 - Exibir linhas que contém um termo")
    print("3 - Exibir a contagem dos tipos de logs")
    print("0 - Sair")
    print("-"*40)
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        arquivo.seek(0)
        for linha in arquivo:
            print(linha.strip())
    elif opcao == 2:
        termo = input("Digite o termo que deseja buscar: ")
        arquivo.seek(0) # mover o cursor para o inicio do arquivo
        for linha in arquivo:
            print(linha)
    elif opcao == 3:
        arquivo.seek(0)
        total_error = 0
        total_warning = 0
        total_info = 0
        for linha in arquivo:
            if 'ERROR' in linha:
                total_error += 1
            elif 'WARNING' in linha:
                total_warning += 1
            elif 'INFO' in linha:
                total_info += 1

        print(f"Total INFO: {total_info}")
        print(f"Total WARNING: {total_warning}")
        print(f"Total ERROR: {total_error}")

    elif opcao == 0:
        break
    else:
        print("Opção inválida")


arquivo.close()