# Exercício 24 - Listas
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Dada a lista [5, 12, 8, 20, 3, 15], informe quantos itens são maiores que 10.

lista_dados = [5, 12, 8, 20, 3, 15]

contador_maiores_que_dez = 0

for numero in lista_dados:
    if numero > 10:
        contador_maiores_que_dez += 1

print(f"Quantidade de itens maiores que 10: {contador_maiores_que_dez}")
