try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero!")

except ValueError:
    print("Erro: entrada inválida! Por favor, digite apenas números.")
    
else:
    print(f"O resultado da divisão é: {resultado}")
    print("Divisão realizada com sucesso!")