try:
    num = int(input("Digite um número inteiro: "))
    print(f"Você digitou: {num}")
except ValueError:
    print("Erro! Isso não é um número inteiro válido.")
