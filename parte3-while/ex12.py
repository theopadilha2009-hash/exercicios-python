# Exercício 12 - Repetição com while
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma_total = 0.0
numero_digitado = float(input("Digite um número (ou 0 para parar): "))

while numero_digitado != 0:
    soma_total += numero_digitado
    numero_digitado = float(input("Digite outro número (ou 0 para parar): "))

print(f"A soma de todos os números digitados é: {soma_total}")
