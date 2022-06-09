################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos

Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""

def superposicion(lista1, lista2):
    """
    Esta funcion se encarga de retornar un numero con la cantidad de caracteres
    (incluidos espacios) que se superponen en una palabra o frase.
    """
    contador = 0
    superpos = 0
    if len(lista1) > len(lista2):
        while contador < len(lista2):
            if lista1[contador] == lista2[contador]:
                superpos += 1
            contador += 1
    else:
        while contador < len(lista1):
            if lista2[contador] == lista1[contador]:
                superpos += 1
            contador += 1
    return superpos


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista1 = ['h', 'a', 'c', 'e', ' ', 'c', 'a', 'l', 'o', 'r']
    lista2 = ['h', 'a', 'c', 'e', ' ', 'f', 'r', 'i', 'o']
    print(superposicion(lista1, lista2))


if __name__ == "__main__":
    principal()
