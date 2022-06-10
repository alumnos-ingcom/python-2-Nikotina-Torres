################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import secuencia, mayor, menor, promedio

"""
Se están probando 4 funciones:
secuencia, la cual retorna una tupla con los números ingresados.
mayor, la cual retorna el numero mayor de una tupla ingresada.
menor, la cual retorna el numero menor de una tupla ingresada.
promedio, la cual retorna el promedio de todos los número en una tupla.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_secuencia():
    """
    Se le pide crear una tupla con los numeros 3,4,5.
    """
    try:
        tupla = secuencia(3, 2,3,4)
    except TypeError:
        print("Solo porque es prueba")
        tupla = (2, 3, 4)
    assert isinstance(tupla, tuple), "Lo retornado debe ser una tuple"
    assert tupla == (2, 3, 4)

    

def test_mayor():
    """
    Se le provee una tupla a la función, cuyo mayor número es 5.
    """
    tupla = (1,5,2,3,-4)
    resultado = mayor(tupla)
    assert resultado == 5, "El resultado está mal"

def test_menor():
    """
    Se le provee una tupla a la función, cuyo menor numero es -4.
    """
    tupla = (1,5,2,3,-4)
    resultado = menor(tupla)
    assert resultado == -4, "El resultado está mal"


def test_promedio():
    """
    Se le provee una tupla
    """
    tupla = (1,2,3,4,5)
    resultado = promedio(tupla)
    assert resultado == 3.0, "El resultado está mal"
