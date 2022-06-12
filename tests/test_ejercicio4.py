################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import fibonacci

"""
Probando funcion que se encarga de que cada elemento sea la suma de los dos anteriores.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_fibonacci():
    """
    Se probará con el primer termino y el sexto de la sucesión.
    """
    numero_sucecion = 0
    resultado = fibonacci(numero_sucecion)
    assert resultado == 1, "El resultado del primer termino debe ser 1"
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
    numero_sucecion = 5
    resultado = fibonacci(numero_sucecion)
    assert resultado == 8, "El resultado del sexto termino debe ser 8"
    assert isinstance(resultado, int), "El resultado debe ser un numero entero"
