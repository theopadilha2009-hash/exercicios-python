# Exercício 04 - Variáveis, entrada e saída
# Enunciado: Peça uma temperatura em graus Celsius e converta para Fahrenheit. A fórmula é F = C × 9 / 5 + 32.

temperatura_celsius = float(input("Digite a temperatura em graus Celsius (°C): "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

print(f"{temperatura_celsius}°C equivalem a {temperatura_fahrenheit:.2f}°F")
