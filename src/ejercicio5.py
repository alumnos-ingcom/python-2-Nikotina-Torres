################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados

Implementar una función que determine si una cadena con corchetes está balanceada.

Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.
"""
def cadena_balanceada(cadena):
    corchete_abierto = 0
    corchete_cerrado = 0
    contador = 0
    for i in cadena:
        if cadena[contador] == "[":
            corchete_abierto += 1
            contador += 1
        elif cadena[contador] == "]":
            corchete_cerrado += 1
            contador += 1
        else:
            contador += 1
    if corchete_abierto == 0 and corchete_cerrado == 0:
        return False
    elif corchete_abierto == corchete_cerrado:
        return True
    else:
        return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = "[testo]]"
    print(cadena_balanceada(cadena))


if __name__ == "__main__":
    principal()
