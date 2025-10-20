# Função de Média
def calcular_media(notas):
  return sum(notas) / len(notas)

notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
media = calcular_media(notas)
print(f"A média é: {media:.2f}")