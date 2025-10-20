# Programa: Verificar a média de 3 notas e informa se o aluno está aprovado ou reprovado

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processamento
media = (nota1 + nota2 + nota3) / 3

# Saída de dados
print(f"\nMédia final: {media:.2f}")  # Mostra a média com duas casas decimais

if media >= 7:
    print("Aluno está APROVADO! 🎉")
else:
    print("Aluno está REPROVADO. 😞")

# Fim do programa