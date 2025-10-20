from pacote import ex9_funcoes_basicas, ex10_funcoes_avancadas

# Teste das funções importadas
resultado_soma  = ex9_funcoes_basicas.soma(int(input("Digite o primeiro número para soma:")), int(input("Digite o segundo número para soma:")))

resultado_sub = ex9_funcoes_basicas.subtracao(int(input("Digite o minuendo:")), int(input("Digite o subtraendo:")))

resultado_pot = ex10_funcoes_avancadas.potenciacao(int(input("Digite a base:")), int(input("Digite o expoente:")))

resultado_raiz = ex10_funcoes_avancadas.raiz_quadrada(int(input("Digite um número para calcular a raiz quadrada:")))

# Exibindo os resultados
print("Soma:", resultado_soma)
print("Subtração:", resultado_sub)
print("Potenciação:", resultado_pot)
print("Raiz Quadrada:", resultado_raiz)