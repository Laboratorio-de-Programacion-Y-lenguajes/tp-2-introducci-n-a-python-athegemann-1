# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    # TU CÓDIGO AQUÍ
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    # resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return lista


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    lista = []
    for i in range(1, 11):
        lista.append(n * i)
    return lista


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    total = 0
    for digito in str(n):
        total += int(digito)
    return total


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n == 0:
        return []
    lista = [0]
    if n == 1:
        return lista
    lista.append(1)
    for i in range(2, n):
        lista.append(lista[i - 1] + lista[i - 2])
    return lista
