################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares

Escribir una función que retorne True cuando un número entero es par y
False cuando no lo sea, sin utilizar módulo. (%)
"""
def es_par(numero):
    """
    Esta función se encarga de retornar True cuando un numero ingresado es
    par, o False si es no lo es.
    """
    contador = 0
    if numero + numero >= 0:
        while contador < numero:
            contador += 2
        if contador == numero:
            return True
        else:
            return False
    elif numero + numero <0:
        while contador > numero:
            contador -= 2
        if contador == numero:
            return True
        else:
            return False
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número entero... "))
    if es_par(numero) is True:
        print(f"{numero} es par")
    else:
        print(f"{numero} NO es par")

if __name__ == "__main__":
    principal()
