# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    limpio = texto.lower().replace(" ", "")
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    capitalizadas = []
    for palabra in palabras:
        capitalizadas.append(palabra.capitalize())
    return " ".join(capitalizadas)


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiouAEIOU"
    conteo = 0
    for char in texto:
        if char in vocales:
            conteo += 1
    return conteo


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            nuevo = chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado += nuevo
        elif 'A' <= char <= 'Z':
            nuevo = chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
            resultado += nuevo
        else:
            resultado += char
    return resultado
