total_notas = 0
contador = 0

with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split("-")
        nota = float(nota.strip())
        print(f"Aluno: {nome.strip()}, Nota: {nota}")
        total_notas += nota
        contador += 1

if contador > 0:
    media = total_notas / contador
    print(f"\nMédia das notas da turma: {media:.2f}")
else:
    print("Nenhuma nota registrada no arquivo.")
