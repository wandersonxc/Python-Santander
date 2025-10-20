with open("notas.txt", "r") as arquivo:
    for linha in arquivo:
        nome, nota = linha.strip().split("-")
        print(f"Aluno: {nome.strip()}, Nota: {nota.strip()}")