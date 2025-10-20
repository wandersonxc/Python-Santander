# .upper() → tudo MAIÚSCULO

# .lower() → tudo minúsculo

# .title() → primeira letra maiúscula

# .strip() → remove espaços extras

# .replace() → troca palavras ou letras


texto = "python é legal"
print(texto.upper()) #tudo MAIÚSCULO     

texto2 = "APRENDENDO PYTHON"
print(texto2.lower()) #tudo minúsculo

texto3 = "estou aprendendo python"
print(texto3.title()) #primeira letra maiúscula

texto4 = "   Wanderson   "
print(texto4.strip()) #remove espaços antes e depois da string

texto5 = "Eu gosto de Java"
print(texto5.replace("Java", "Python")) #troca a palavra Java por Python