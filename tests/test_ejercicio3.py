################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import superposicion

"""
Se prueba la función superposicion que retorna el numero de caracteres
superpuestos entre dos listas.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_superposicion():
    """
    Se prueban listas totalmente distintas, totalmente idénticas y parcialmente
    iguales.
    """
    lista1 = ("h", "o", "l", "a", " ", "q", "u", "e", "s", "o")
    lista2 = ("h", "o", "l", "a", " ", "q", "u", "e", "s", "o")
    resultado = superposicion(lista1, lista2)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 10, "El resultado es incorrecto"
    lista1 = ("h", "o", "l", "a", " ", "q", "u", "e", "s", "o")
    lista2 = ("c", "h", "a", "u", "j", "a", "m", "o", "n")
    resultado = superposicion(lista1, lista2)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 0, "El resultado es incorrecto"
    lista1 = ("h", "o", "l", "a", " ", "q", "u", "e", "s", "o")
    lista2 = ("h", "o", "l", "a", " ", "j", "a", "m", "o", "n")
    resultado = superposicion(lista1, lista2)
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    assert resultado == 5, "El resultado es incorrecto"
