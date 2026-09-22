# Exercício 05 - Variáveis, entrada e saída
# Estudante: Theo Lorentz Padilha - Turma: DSM3-25
# Enunciado: Peça o preço de um produto e a quantidade comprada. Exiba o valor total, com duas casas decimais.

preco_unitario = float(input("Digite o preço do produto (R$): "))
quantidade_comprada = int(input("Digite a quantidade comprada: "))

valor_total = preco_unitario * quantidade_comprada

print(f"Valor total a pagar: R$ {valor_total:.2f}")
