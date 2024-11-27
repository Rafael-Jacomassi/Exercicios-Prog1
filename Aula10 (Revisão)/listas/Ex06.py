"""
Filtrar Logs de Erro
Dada uma lista de logs de sistema, filtre apenas os logs que contenham a palavra "ERRO".

Saída Esperada:
["ERRO: Falha na conexão", "ERRO: Permissão negada"]
"""

logs = ["INFO: Sistema iniciado", "ERRO: Falha na conexão", "DEBUG: Verificação completa", "ERRO: Permissão negada"]
erros = []

for log in logs:
    separado = log.split(":")[0]
    if separado == "ERRO":
        erros.append(log)
print(erros)