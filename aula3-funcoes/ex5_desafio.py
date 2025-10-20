# Desafio - Boletim de vários alunos usando funções

def adicionar_aluno(num_notas=2):
    """Adiciona um aluno à lista e retorna os dados.
    Permite definir a quantidade de notas."""
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome:
            break
        print("Erro: o nome não pode ficar vazio.")

    notas = []
    for i in range(num_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Erro: nota deve estar entre 0 e 10.")
            except ValueError:
                print("Erro: digite apenas números válidos.")

    media = sum(notas) / len(notas)
    status = "APROVADO" if media >= 7 else "REPROVADO"

    return [nome, notas, media, status]

def exibir_boletim(alunos):
    """Exibe o boletim de todos os alunos."""
    print("\nNº   NOME                 MÉDIA   STATUS")
    print("-" * 45)
    for i, aluno in enumerate(alunos):
        print(f"{i:<4} {aluno[0]:<20} {aluno[2]:<7.2f} {aluno[3]:<10}")

def consultar_notas(alunos):
    """Permite consultar as notas individuais dos alunos."""
    while True:
        try:
            opcao = int(input("\nMostrar notas de qual aluno? (999 interrompe): "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 999:
            print("Finalizando consulta...")
            break
        if 0 <= opcao < len(alunos):
            print(f"Notas de {alunos[opcao][0]}: {alunos[opcao][1]}")
        else:
            print("Número inválido. Tente novamente.")

# Programa principal
alunos = []
while True:
    alunos.append(adicionar_aluno())
    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Exibe o boletim completo
exibir_boletim(alunos)

# Consulta de notas individuais
consultar_notas(alunos)
