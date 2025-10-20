frase = input("Digite uma frase: ")
caracter1 = frase[0]
primeiros5 = frase[:5]
ultimos5 = frase[-5:] 
tamanhoFrase = len(frase)
fraseInvertida = frase[::-1]

print(f"Primeiro caractere: {caracter1}")
print(f"Primeiros 5 caracteres: {primeiros5}")
print(f"Últimos 5 caracteres: {ultimos5}")
print(f"Tamanho da frase: {tamanhoFrase}")
print(f"Frase invertida: {fraseInvertida}")