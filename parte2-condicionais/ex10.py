# Exercício 10 - Condicionais
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça a idade de uma pessoa e informe se ela já pode votar. A idade mínima é 16 anos.

idade_pessoa = int(input("Digite a idade da pessoa: "))

if idade_pessoa >= 16:
    print(f"Com {idade_pessoa} anos, a pessoa já pode votar.")
else:
    print(f"Com {idade_pessoa} anos, a pessoa ainda não pode votar (idade mínima: 16 anos).")
