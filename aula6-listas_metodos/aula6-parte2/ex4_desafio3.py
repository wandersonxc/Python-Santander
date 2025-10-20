boletim = [
    ["Ana Paula", 8.0, 8.5],
    ["Lucas Lorenzo", 9.5, 8.5],
    ["Anthony Gabriel", 9.0, 9.0]
]

# Desafio 3: Lista com as médias dos alunos usando list comprehension
medias = [ (aluno[1] + aluno[2]) / 2 for aluno in boletim ]
print(medias)