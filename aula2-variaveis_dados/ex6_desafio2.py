# Desafio 2 - Média com Conceito

# Entrada de dados
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Validação simples das notas
if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10):
    print("Erro: todas as notas devem estar entre 0 e 10.")
    exit()

# Processamento
media = (nota1 + nota2 + nota3) / 3

# Definição de conceito e status
if media >= 9.0:
    conceito = 'A'
    status = "APROVADO! 🎉"
elif media >= 7.0:
    conceito = 'B'
    status = "APROVADO! 🎉"
elif media >= 5.0:
    conceito = 'C'
    status = "REPROVADO. 😞"
else:
    conceito = 'D'
    status = "REPROVADO. 😞"

# Saída de dados
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")

# Fim do programa   