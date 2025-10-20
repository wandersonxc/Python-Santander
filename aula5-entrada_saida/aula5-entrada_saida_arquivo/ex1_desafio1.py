with open("notas.txt", "w") as arquivo:
    for i in range(3):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota = input(f"Digite a nota do aluno {i+1}: ")
        arquivo.write(f"{nome} - {nota}\n")