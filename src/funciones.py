# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna una nueva lista.

    No normaliza ni limpia los elementos antes de aplicar la función:
    por ejemplo, "hola," y "hola" se tratan como valores distintos.
    """
    return [func(elemento) for elemento in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def compuesta(x):
        return f(g(x))

    return compuesta


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}

    def envuelta(*args, **kwargs):
        clave = (args, tuple(sorted(kwargs.items())))
        if clave in cache:
            return cache[clave]

        resultado = func(*args, **kwargs)
        cache[clave] = resultado
        return resultado

    return envuelta


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    acumulado = inicial
    for elemento in lista:
        acumulado = func(acumulado, elemento)
    return acumulado
