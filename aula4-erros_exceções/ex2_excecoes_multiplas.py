try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    resultado = a / b
except ValueError:
    print("Erro: digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Fim do programa.")