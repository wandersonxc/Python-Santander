nome = input("Digite seu nome: ")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro: digite apenas números para a idade!")

print(f"Nome cadastrado: {nome}")
print(f"Idade cadastrada: {idade}")