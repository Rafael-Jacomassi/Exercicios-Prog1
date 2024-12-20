# Função de Contagem de Palavras
# Descrição: Crie uma função chamada contar_palavras que recebe uma string como parâmetro e
# retorna o número de palavras na string.

def contar_palavras(frase):
    frase_limpa = frase.replace(",", "").replace(".","")
    palavras = frase_limpa.split(" ")
    return len(palavras)


frase = "O sucesso não é determinado por quantas vezes você ganha, mas por como você joga na semana após a derrota."
print(contar_palavras(frase))  # 20