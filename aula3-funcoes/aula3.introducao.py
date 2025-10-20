#Uma função é um bloco de código reutilizável, que realiza uma tarefa específica.

# Declaração de Função
def ola_mundo():
    print("Olá, Mundo!")
# A palavra-chave def é usada para declarar uma função, seguida pelo nome da função e parênteses.
ola_mundo()

# Função com Parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a).")

saudacao("Wanderson")

# Função com Retorno
def soma(a, b):
    return a + b

resultado = soma(5, 7)
print(f"A soma é: {resultado}")

# Escopo de Variáveis

x = 10  # Variável global

def testar_escopo():
    y = 5  # Variável local
    print("Dentro da função:", x, y)  # A função consegue acessar a global e a local

testar_escopo()

print("Fora da função:", x)  # A variável global está disponível fora da função

# print(y)  # Isso daria erro, pois 'y' é local da função

# Parâmetros Padrão
def saudacao(nome="Aluno"):
    print(f"Olá, {nome}!")

saudacao()  # Usa o valor padrão
saudacao("Wanderson")   # Sobrescreve o valor padrão