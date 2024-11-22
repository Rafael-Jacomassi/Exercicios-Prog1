# Função de Extração de Domínio de Email
# Descrição: Crie uma função chamada extrair_dominio que recebe um endereço de email como parâmetro
# e retorna o domínio do email.

'''def extrair_dominio(email):
    posicao_arroba = email.find("@")
    dominio = email[posicao_arroba + 1: ]
    return dominio'''

def extrair_dominio(email):
    email_separado = email.split("@")
    return email_separado[-1]


lista_emails = ["usuario@fatec.sp.gov.br", "usuario@dominio.com", "nome.sobrenome@empresa.org"]

for email in lista_emails:
    print(extrair_dominio(email))


# resultado esperado:
# fatec.sp.gov.br
# dominio.com
# empresa.org