# Criando uma lista
alunos = ["Ana Paula", "Sophia", "Lucas Lorenzo", "Wanderson", "Lucia"]
notas = [9.5, 8.0, 7.5, 6.0, 10.0]

# Acessando elementos
print(alunos[0])  # Ana Paula
print(notas[0])   # 9.5

# Métodos básicos
alunos.append("Carlos")      # Adiciona no final
alunos.insert(1, "Mariana")  # Adiciona na posição 1
alunos.remove("Lucia")       # Remove o elemento
alunos.pop()                 # Remove o último elemento

print("\nLista final de alunos:", alunos)
print("Lista de notas:", notas)
