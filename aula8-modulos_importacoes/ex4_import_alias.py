import math as m

numero = float(input("Digite um número: "))  # exemplo: 10

raiz = m.sqrt(numero)        # sqrt(10) ≈ 3.162
arredondado = m.ceil(raiz) # ceil(3.162) = 4

print(f"Raiz quadrada: {raiz}")
print(f"Arredondado para cima: {arredondado}")