"""
Crie um programa que analisa uma lista de IPs
e verifica se algum IP realizou
mais de 5 acessos, sinalizando um possível ataque DDoS.

Saída Esperada:
IPs suspeitos de ataque DDoS:
- 192.168.0.1: 5 acessos

Não utilize o método count() para resolver este problema.
"""
ips = [
    "192.168.0.1", "192.168.0.2", "192.168.0.1", "192.168.0.3",
    "192.168.0.1", "192.168.0.1", "192.168.0.2", "192.168.0.1",
    "192.168.0.5", "192.168.0.6", "192.168.0.7", "192.168.0.1"
]

ips_verificados = []

for ip in ips:
    if ip not in ips_verificados:
        contador = 0

        for ipv in ips:
            if ipv == ip:
                contador += 1
        
        if contador > 5:
            print(f"- {ip}: {contador} acessos")
        
        ips_verificados.append(ip)