frase = input("Digite uma frase: ")
palavras = frase.split()

frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

palavra_mais_frequente = ""
maior_quantidade = 0

for palavra, quantidade in frequencia.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        palavra_mais_frequente = palavra

print("Resultado:", frequencia)
print(f"Palavra mais frequente: '{palavra_mais_frequente}' ({maior_quantidade} vezes)")