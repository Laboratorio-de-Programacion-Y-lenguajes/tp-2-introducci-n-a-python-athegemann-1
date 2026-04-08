# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    Ejemplo: crear_saludo("Ana") -> "Hola, Ana!"
    """
    # TU CÓDIGO AQUÍ
    pass

def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.
    """
    # TU CÓDIGO AQUÍ
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """
    Retorna True si edad >= 18, False caso contrario.
    """
    # TU CÓDIGO AQUÍ
    return edad >= 18


def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    # TU CÓDIGO AQUÍ
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    # TU CÓDIGO AQUÍ
    return float(valor)