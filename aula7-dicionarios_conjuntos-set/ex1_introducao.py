# Dicionários e Conjuntos (set)

# Dicionários são estruturas de dados que armazenam pares de chave-valor.
aluno = {"nome": "Ana Paula", "nota1": 8.0, "nota2": 8.5}
print(aluno["nome"])   # Ana Paula

# Adicionar ou alterar valores:
aluno["nota3"] = 9.0
aluno["nome"] = "Ana P."

# Remover Elemento:
del aluno["nota2"]

# Iterar sobre dicionário:
for chave, valor in aluno.items():
    print(chave, valor)

# Conjuntos (set), Armazenam elementos únicos. Sintaxe:
frutas = {"maçã", "banana", "laranja", "maçã"}  # "maçã" duplicada será ignorada
print(frutas)

# Adicionar ou remover elementos:
frutas.add("uva")
frutas.remove("banana")
print(frutas)
