def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    return f"Idade válida: {idade}"

try:
    print(verificar_idade(-5))
except ValueError as e:
    print(f"Erro detectado: {e}")
