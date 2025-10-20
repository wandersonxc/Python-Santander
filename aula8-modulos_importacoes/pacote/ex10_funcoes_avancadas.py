def potenciacao(a, b):
    return a ** b

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def raiz_quadrada(n):
    return n ** 0.5