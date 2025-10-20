# Lista inicial de alunos e notas
alunos = ["Ana", "João", "Maria", "Paulo", "Beatriz"]
notas = [8.5, 7.0, 9.2, 6.8, 10.0]

# Adicionando mais 2 alunos e suas notas
alunos.append("Carlos")
notas.append(7.5)

alunos.append("Fernanda")
notas.append(8.8)

# Substituindo a nota do aluno do índice 2 (Maria)
notas[2] = 9.8

# Removendo o último aluno e sua nota
alunos.pop()
notas.pop()

# Mostrando os resultados finais
print("Lista final de alunos:", alunos)
print("Lista final de notas:", notas)
print("Total de alunos:", len(alunos))