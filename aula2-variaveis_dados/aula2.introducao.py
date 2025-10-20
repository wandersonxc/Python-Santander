# O nome da variável é como a etiqueta da caixa, e o valor é o conteúdo.
# Exemplos de declaração de variáveis em Python

nome = "Wanderson"
idade = 33
altura = 1.66
casado = True

print(nome, idade, altura, casado)

# Tipos de Dados em Python
# Exemplos de tipos de dados comuns em Python

nome = "Wanderson"  # texto (String)
idade = 33          # Números Inteiros
altura = 1.66       # Números Decimais (Float)
tem_filhos = True   # Valor lógico (Booleano-Verdadeiro/Falso)

print(nome, idade, altura, tem_filhos)

# Verificação de tipos de dados
# Exemplo de verificação de tipos de dados em Python
print(type(nome))      # <class 'str'>
print(type(idade))     # <class 'int'>
print(type(altura))    # <class 'float'>
print(type(tem_filhos))# <class 'bool'>
# O tipo de dado informa ao Python como ele deve interpretar o valor armazenado na variável.

# Conversão de tipos de dados
# Exemplo de conversão de tipos de dados em Python

idade = "33"
idade = int(idade)
print(idade + 1)  # 34

#int() → converte pra inteiro
#float() → converte pra decimal
#str() → converte pra texto
#bool() → converte pra verdadeiro/falso

#Interação com o usuário
# Exemplo de interação com o usuário em Python

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"Olá, {nome}! Você tem {idade} anos.")

# A função input() lê uma entrada do usuário como texto (string).