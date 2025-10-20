# Loop for em listas
alunos = ["Ana", "João", "Maria"]
for aluno in alunos:
    print(aluno)

# Loop while em listas
numeros = [1, 2, 3, 4, 5]
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1

# listas de listas
boletim = [
    ["Ana Paula", 8.5, 7.0],
    ["João Pedro", 6.0, 9.5],
    ["Maria Clara", 10.0, 8.5]
]

for aluno in boletim:
    print(f"{aluno[0]} - Notas: {aluno[1]}")

# Acessando elementos individuais
print(boletim[1][0])
print(boletim[2][2])