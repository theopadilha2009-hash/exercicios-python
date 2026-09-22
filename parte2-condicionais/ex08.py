# Exercício 08 - Condicionais
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça um número e informe se ele é positivo, negativo ou igual a zero.

numero_avaliado = float(input("Digite um número: "))

if numero_avaliado > 0:
    print(f"O número {numero_avaliado} é positivo.")
elif numero_avaliado < 0:
    print(f"O número {numero_avaliado} é negativo.")
else:
    print("O número informado é igual a zero.")
