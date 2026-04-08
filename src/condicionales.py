# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cerro" según corresponda.
    Si el valor no es int, retorna "error".
    """
    if type(n) is not int:
        return "error"
    if n > 0:
        return "positivo"
    if n < 0:
        return "negativo"
    return "cero"


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números.
    """
    # TU CÓDIGO AQUÍ
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota:
    - nota >= 9: "Sobresaliente"
    - nota >= 7: "Bueno"
    - nota >= 6: "Aprobado"
    - nota < 6:  "Desaprobado"
    """
    # TU CÓDIGO AQUÍ
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto.
    Un año es bisiesto si es divisible por 4,
    excepto los divisibles por 100, salvo que también lo sean por 400.
    """
    # TU CÓDIGO AQUÍ
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
