# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(lista: list[int]) -> int:
    """Devuelve la suma de todos los elementos enteros de una lista."""
    total = 0
    for elemento in lista:
        total += elemento
    return total

def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    # TU CÓDIGO AQUÍ
    invertida = []
    for i in range(len(lista)):
        invertida.append(lista[len(lista) - 1 - i])
    return invertida


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    resultado = []
    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado
