# Exercício 14 - Repetição com while
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça um número e exiba sua tabuada de 1 a 10.

numero_base = int(input("Digite um número para ver sua tabuada: "))
multiplicador = 1

while multiplicador <= 10:
    resultado_multiplicacao = numero_base * multiplicador
    print(f"{numero_base} x {multiplicador} = {resultado_multiplicacao}")
    multiplicador += 1
