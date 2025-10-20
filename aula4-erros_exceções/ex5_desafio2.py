nomes = ["Ana", "João", "Maria", "Paulo", "Beatriz"]

try:
    indice = int(input("Digite o índice do nome que deseja ver: "))
    print(f"Nome escolhido: {nomes[indice]}")
except ValueError:
    print("Erro: por favor, digite apenas números.")
except IndexError:
    print("Erro: índice fora do intervalo!")