# Exercício 22 - Listas
# Enunciado: Usando a lista do exercício anterior, calcule e exiba a soma de todos os itens.

lista_numeros = [14, 28, 35, 42, 56]

soma_elementos = 0

for numero in lista_numeros:
    soma_elementos += numero

print(f"A soma de todos os itens da lista é: {soma_elementos}")
