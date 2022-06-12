################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import cadena_balanceada

"""
Probando la función que se encarga de verificar que todos los corchetes
de una cadena tengan una 'apertura' y una 'cerradura'. 
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_cadena_balanceada():
    """
    Se probará una cadena con todos los corchetes 'completos' y otra que no.
    """
    cadena = "[[hola][probando]][esto]"
    resultado = cadena_balanceada(cadena)
    assert resultado is True, "El resultado debe ser verdadero"
    assert isinstance(resultado, bool), "El resultado debe ser True or False"
    cadena = "[estos][corchetes][estan incompletos"
    resultado = cadena_balanceada(cadena)
    assert resultado is False, "El resultado debe ser Falso"
    assert isinstance(resultado, bool), "El resultado debe ser True or False"
