boletim = [
    ["Ana Paula", 8.0, 8.5],
    ["Lucas Lorenzo", 9.5, 8.5],
    ["Anthony Gabriel", 9.0, 9.0]
]

for aluno in boletim:
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f"{nome} - Média: {media:.2f}")