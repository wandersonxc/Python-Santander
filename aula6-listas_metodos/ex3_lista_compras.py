compras = ["arroz", "feijão", "macarrão"]

# Adicionando itens à lista de compras
compras.append("leite")
compras.append("pão")

# Substituindo item do índice 1
compras[1] = "feijão carioca"

# Removendo o último item da lista
compras.pop()

print("Lista final de compras:", compras)
print("Total de itens:", len(compras))