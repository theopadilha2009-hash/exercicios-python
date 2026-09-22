# Exercício 07 - Condicionais
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"O maior número é: {primeiro_numero}")
elif segundo_numero > primeiro_numero:
    print(f"O maior número é: {segundo_numero}")
else:
    print("Os dois números informados são iguais.")
