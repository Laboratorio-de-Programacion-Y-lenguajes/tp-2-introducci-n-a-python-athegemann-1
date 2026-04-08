import pytest
from src.variables import (
    crear_saludo,
    suma_enteros,
    es_mayor_de_edad,
    tipo_de_dato,
    convertir_a_float,
)


def test_crear_saludo_simple():
    assert crear_saludo("Ana") == "Hola, Ana!"


def test_crear_saludo_otro_nombre():
    assert crear_saludo("Juan") == "Hola, Juan!"


def test_suma_enteros_positivos():
    assert suma_enteros(3, 4) == 7


def test_suma_enteros_negativos():
    assert suma_enteros(-2, -3) == -5


def test_suma_enteros_mixtos():
    assert suma_enteros(-1, 1) == 0


def test_es_mayor_de_edad_true():
    assert es_mayor_de_edad(18) is True
    assert es_mayor_de_edad(25) is True


def test_es_mayor_de_edad_false():
    assert es_mayor_de_edad(17) is False
    assert es_mayor_de_edad(0) is False


def test_tipo_de_dato_int():
    assert tipo_de_dato(42) == "int"


def test_tipo_de_dato_str():
    assert tipo_de_dato("hola") == "str"


def test_tipo_de_dato_float():
    assert tipo_de_dato(3.14) == "float"


def test_tipo_de_dato_bool():
    assert tipo_de_dato(True) == "bool"


def test_convertir_a_float():
    assert convertir_a_float("3.14") == 3.14
    assert convertir_a_float("0") == 0.0
