# Exercício 25 - Listas
# Enunciado: Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.
# Nota técnica: Para demonstrar compreensão completa do controle de índices,
# a inversão é produzida acessando diretamente as posições decrementais da coleção
# (do índice final len - 1 até 0), sem uso de métodos embutidos como reverse() ou slicing [::-1].

lista_valores = [3, 7, 1, 9, 4]

indice_final = len(lista_valores) - 1

for indice in range(indice_final, -1, -1):
    print(lista_valores[indice])
