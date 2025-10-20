# Desafio Extra 3 - Boletim de vários aunos

# Lista principal para armazenar todos os alunos
alunos = []

while True:
    # Entrada de dados
    nome = input("Nome: ")

    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
    except ValueError:
        print("Erro: digite apenas números válidos para as notas.")
        continue

    # Validação das notas
    if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
        print("Erro: notas devem estar entre 0 e 10.")
        continue

    # Cálculo da média e definição do status
    media = (nota1 + nota2) / 2
    status = "APROVADO" if media >= 7 else "REPROVADO"

    # Adiciona os dados do aluno na lista
    alunos.append([nome, [nota1, nota2], media, status])

    # Pergunta se deseja continuar
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Exibe boletim resumido
print("\nNº   NOME           MÉDIA   STATUS")
print("-" * 40)
for i, aluno in enumerate(alunos):
    print(f"{i:<4} {aluno[0]:<15} {aluno[2]:<7.2f} {aluno[3]:<10}")

# Permite consultar notas individuais
while True:
    try:
        opcao = int(input("\nMostrar notas de qual aluno? (999 interrompe): "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 999:
        print("Finalizando...")
        break
    if 0 <= opcao < len(alunos):
        print(f"Notas de {alunos[opcao][0]}: {alunos[opcao][1]}")
    else:
        print("Número inválido. Tente novamente.")

# Fim do programa