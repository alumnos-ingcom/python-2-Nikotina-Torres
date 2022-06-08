################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas

Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
def estadisticas(n1, n2, n3):
    tupla = list()
    if n1 > n2 and n1 > n3:
        tupla.append(n1)
        if n2 > n3:
            tupla.insert(n2, n3)
        else:
            tupla.insert(n3, n2)
    elif n2 > n1 and n2 > n3:
        tupla.append(n2)
        if n1 > n3:
            tupla.insert(n1, n3)
        else:
            tupla.insert(n3, n1)
    else:
        tupla.append(n3)
        if n2 > n1:
            tupla.insert(n2, n1)
        else:
            tupla.insert(n1, n2)
    tupla.append((n1+n2+n3)/3)
    return tuple(tupla)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1= int(input("Ingrese numero... "))
    numero2= int(input("Ingrese numero... "))
    numero3= int(input("Ingrese numero... "))
    resultado = estadisticas(numero1, numero2, numero3)
    print(f"Máximo: {resultado[0]} Mínimo: {resultado[1]} Promedio: {resultado[2]}")


if __name__ == "__main__":
    principal()
