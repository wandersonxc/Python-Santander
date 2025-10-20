# dicionario aluno com nome, nota1, nota2, calcule média e adicione ao dicionario com a chave "media", imprimindo o dicionario completo
aluno = {
    "nome": "Ana Paula",
    "nota1": 8.0,
    "nota2": 8.5
}

media = (aluno["nota1"] + aluno["nota2"]) / 2
aluno["media"] = media

print(aluno)