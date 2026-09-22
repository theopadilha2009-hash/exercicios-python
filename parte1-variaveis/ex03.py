# Exercício 03 - Variáveis, entrada e saída
# Enunciado: Peça o raio de um círculo e calcule a área. Use 3.14159 como valor de pi.

raio_circulo = float(input("Digite o raio do círculo: "))
valor_pi = 3.14159

area_circulo = valor_pi * (raio_circulo ** 2)

print(f"A área do círculo com raio {raio_circulo} é: {area_circulo:.4f}")
