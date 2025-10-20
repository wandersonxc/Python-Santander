# Conta a frequência de cada palavra na frase
frase = input("Digite uma frase: ")
palavras = frase.split()

frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("Resultado:", frequencia)