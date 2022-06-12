################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import cifrar, decifrar

"""
Se prueba la funcion que codifica strings que usen los sig. caracteres:
A-Z, a-z, 0-9
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_cifrar():
    """
    Se codificará un string.
    """
    string = "az90AZ"
    movimientos = 1
    cifrado = cifrar(string, movimientos)
    assert cifrado == "ba01BA", "El cifrado salió mal"
    assert isinstance(cifrado, str), "El cifrado debe ser un string"

def test_decifrar():
    """
    Se decifrará el anterior cifrado.
    """
    string = "ba01BA"
    movimientos = 1
    decifrado = decifrar(string, movimientos)
    assert decifrado == "az90AZ", "El decifrado salió mal"
    assert isinstance(decifrado, str), "El decifrado debe ser un string"
