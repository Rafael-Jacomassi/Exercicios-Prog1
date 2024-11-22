"""
Escreva um programa que gera um endereço de email.
Peça ao usuário seu nome e sobrenome e então gere um email no formato
nome.sobrenome@gmail.com.
Entrada:
Digite seu nome: Maria
Digite seu sobrenome: Silva
Saída:
Seu email é maria.silva@gmail.com
"""

nome = str(input("\nDigite seu nome: ")).lower()
sobrenome = str(input("\nDigite seu sobrenome: ")).lower()

print(f"\nSeu email é {nome}.{sobrenome}@gmail.com\n")