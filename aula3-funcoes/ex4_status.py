# Função de Status
def status_aluno(media):
  if media >= 7:
    return "Aprovado"
  elif media >= 5:
    return "Recuperação"
  else:
    return "Reprovado"
  
media = float(input("Digite a média do aluno: "))
print(f"Status: {status_aluno(media)}")