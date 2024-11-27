'''Crie um programa em Python que receba uma lista de endereços de e-mail corporativos e extraia os 
domínios (o nome da empresa seguido da extensão, como "google.com"). Certifique-se de exibir 
apenas os domínios únicos, sem repetições.'''

emails = [  
"joao@google.com", "maria@apple.com", "carlos@microsoft.com", "ana@google.com", 
"paulo@amazon.com", "lucas@apple.com" 
]
domínios_verificados = []
domínios = []

for email in emails:
    separado = email.split("@")
    domínios.append(separado[1])

for domínio in domínios:
    if domínio not in domínios_verificados:
        domínios_verificados.append(domínio)
        
print(domínios_verificados)