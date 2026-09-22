# Exercício 09 - Condicionais
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça a média de um estudante e classifique:
# 6 ou mais é Aprovado; de 4 a 5,9 é Recuperação; abaixo de 4 é Reprovado.

media_estudante = float(input("Digite a média final do estudante: "))

if media_estudante >= 6.0:
    print(f"Média {media_estudante:.1f}: Aprovado")
elif media_estudante >= 4.0:
    print(f"Média {media_estudante:.1f}: Recuperação")
else:
    print(f"Média {media_estudante:.1f}: Reprovado")
