# Exercício 19 - Repetição com for
# Enunciado: Peça um número e calcule seu fatorial. O fatorial de 5 é 5 × 4 × 3 × 2 × 1 = 120.

numero_informado = int(input("Digite um número para calcular o fatorial: "))

fatorial_calculado = 1

for multiplicador in range(1, numero_informado + 1):
    fatorial_calculado *= multiplicador

print(f"O fatorial de {numero_informado} é: {fatorial_calculado}")
