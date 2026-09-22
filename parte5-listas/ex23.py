# Exercício 23 - Listas
# Enunciado: Usando a mesma lista, encontre e exiba o maior valor.

lista_numeros = [14, 28, 35, 42, 56]

# Inicialização adequada com o primeiro elemento da lista
maior_valor = lista_numeros[0]

for numero in lista_numeros:
    if numero > maior_valor:
        maior_valor = numero

print(f"O maior valor encontrado na lista é: {maior_valor}")
