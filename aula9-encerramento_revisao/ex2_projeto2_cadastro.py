# Controle de Produtos
# Cadastrar produtos com nome, quantidade e preço
produtos = []

for i in range(3):  # cadastra 3 produtos como exemplo
    nome = input(f"Digite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade de {nome}: "))
    preco = float(input(f"Digite o preço de {nome}: "))
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    produtos.append(produto)

print("\nProdutos cadastrados com sucesso!")

#Consultar a lista completa de produtos
print("\nLista de Produtos:")
for produto in produtos:
    print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}")

#Consultar um produto específico pelo nome
while True:
    consulta = input("\nDeseja consultar algum produto específico? (S/N): ").strip().upper()
    if consulta == "N":
        break
    
    nome_consulta = input("Digite o nome do produto: ")
    produto_encontrado = next((p for p in produtos if p['nome'].lower() == nome_consulta.lower()), None)
    
    if produto_encontrado:
        print(f"Produto encontrado - Nome: {produto_encontrado['nome']}, Quantidade: {produto_encontrado['quantidade']}, Preço: {produto_encontrado['preco']:.2f}")
    else:
        print("Produto não encontrado. Tente novamente.")

#Atualizar ou remover produtos
while True:
    acao = input("\nDeseja atualizar ou remover um produto? (A/R/N): ").strip().upper()
    if acao == "N":
        break
    
    nome_acao = input("Digite o nome do produto: ")
    produto_encontrado = next((p for p in produtos if p['nome'].lower() == nome_acao.lower()), None)
    
    if produto_encontrado:
        if acao == "A":
            nova_quantidade = int(input(f"Digite a nova quantidade de {produto_encontrado['nome']}: "))
            novo_preco = float(input(f"Digite o novo preço de {produto_encontrado['nome']}: "))
            produto_encontrado['quantidade'] = nova_quantidade
            produto_encontrado['preco'] = novo_preco
            print("Produto atualizado com sucesso!")
        elif acao == "R":
            produtos.remove(produto_encontrado)
            print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado. Tente novamente.")

# Salvar tudo em um arquivo de texto
with open("produtos_cadastrados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Lista de Produtos:\n")
    for produto in produtos:
        arquivo.write(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: {produto['preco']:.2f}\n")
print("\nDados salvos em 'produtos_cadastrados.txt'.")