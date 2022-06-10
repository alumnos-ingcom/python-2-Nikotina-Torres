################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import es_par

"""
Probando la funcion para saber si un numero es par
o impar, usando numeros pares e impares.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_es_par():
    """
    Probando el numero 12 (par) y el numero 37 (impar).
    """
    numero_par = 12
    numero_impar = 37
    resultado = es_par(numero_par)
    assert isinstance(resultado, bool), "El return debe ser booleano"
    assert resultado is True, "El resultado es incorrecto"
    resultado = es_par(numero_impar)
    assert isinstance(resultado, bool), "El return debe ser booleano"
    assert resultado is False, "El resultado debe ser booleano"
