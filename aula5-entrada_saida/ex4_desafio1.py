# Coleta e faz formatação das informações
nome = input("Digite seu nome: ").strip().title()
cidade = input("Digite sua cidade: ").strip().title()
profissao = input("Digite sua profissão: ").strip().title()

# Validação da idade
while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro: digite apenas números para a idade!")

# Separador visual
print("\n" + "-" * 50)

# Exibição final formatada
print(f"Meu nome é {nome}, tenho {idade} anos, moro em {cidade} e trabalho como {profissao}.")

print("-" * 50)
