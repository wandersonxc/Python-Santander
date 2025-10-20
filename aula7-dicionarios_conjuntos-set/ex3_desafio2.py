# Desafio 2: Cadastro de vários alunos com dicionários
alunos = []

for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")

    while True:
        try:
            nota1 = float(input(f"Digite a nota 1 de {nome}: "))
            nota2 = float(input(f"Digite a nota 2 de {nome}: "))
            break
        except ValueError:
            print("Digite apenas números válidos para as notas!")

    media = (nota1 + nota2) / 2
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media
    }
    alunos.append(aluno)

print("\n📚 BOLETIM FINAL:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Média: {aluno['media']:.2f}")

print("\nLista completa (estrutura bruta):")
print(alunos)