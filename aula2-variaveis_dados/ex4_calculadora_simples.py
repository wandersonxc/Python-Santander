# Peça dois números e mostre a soma, subtração, multiplicação e divisão.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"A soma é: {num1 + num2:.2f}")
print(f"A subtração é: {num1 - num2:.2f}")
print(f"A multiplicação é: {num1 * num2:.2f}")
print(f"A divisão é: {num1 / num2:.2f}")
print(f"O resto da divisão é: {num1 % num2:.2f}")
print(f"A potência é: {num1 ** num2:.2f}")

print("Calculadora simples finalizada.")