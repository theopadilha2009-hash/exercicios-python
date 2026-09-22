# Exercício 15 - Repetição com while
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos foram digitados.

quantidade_positivos = 0
numero_informado = float(input("Digite um número (ou 0 para parar): "))

while numero_informado != 0:
    if numero_informado > 0:
        quantidade_positivos += 1
    numero_informado = float(input("Digite outro número (ou 0 para parar): "))

print(f"Total de números positivos digitados: {quantidade_positivos}")
