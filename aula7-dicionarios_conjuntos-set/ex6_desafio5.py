# Projeto - Boletim de Alunos com Dicionários

alunos = []

# Etapa 1: Cadastro dinâmico
while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    media = (nota1 + nota2) / 2

    aluno = {
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media
    }
    alunos.append(aluno)

    continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().upper()
    if continuar == "N":
        break

# Etapa 2: Boletim completo
print("\nBoletim Completo:")
for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Nota 1: {aluno['nota1']} | Nota 2: {aluno['nota2']} | Média: {aluno['media']:.2f}")

# Etapa 3: Consulta individual
while True:
    consulta = input("\nDeseja consultar as notas de algum aluno? (S/N): ").strip().upper()
    if consulta == "N":
        break

    nome_consulta = input("Digite o nome do aluno: ").strip()
    encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower() == nome_consulta.lower():
            print(f"Notas de {aluno['nome']}: Nota 1 = {aluno['nota1']}, Nota 2 = {aluno['nota2']}, Média = {aluno['media']:.2f}")
            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado. Tente novamente.")

# Etapa 4: Resumo estatístico
total_alunos = len(alunos)
aprovados = sum(1 for aluno in alunos if aluno['media'] >= 7)
reprovados = total_alunos - aprovados
media_geral = sum(aluno['media'] for aluno in alunos) / total_alunos

print("\nResumo da turma:")
print(f"Total de Alunos: {total_alunos}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
print(f"Média geral da turma: {media_geral:.2f}")