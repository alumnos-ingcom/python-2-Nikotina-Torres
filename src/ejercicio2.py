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

def secuencia():
    """
    Esta función se encarga de pedir al usuario un número entero de veces
    para ingresar numeros y añadirlos a una misma lista, que luego se transformará
    en una tupla, retornando esta última.
    """
    lista=list()
    contador = 0
    cantidad = int(input("Cuantos numeros desea ingresar? "))
    while contador < cantidad:
        numero = int(input("Ingrese numero... "))
        lista.append(numero)
        contador += 1
    tuple(lista)
    return lista

def mayor(tupla):
    """
    A esta función se le provee una tupla para que obtenga el numero mayor.
    """
    largo = len(tupla)
    contador = 0
    mayor = int(tupla[0])
    while contador < largo:
        posicion = tupla[contador]
        if posicion > mayor:
            mayor = posicion
            contador += 1
        else:
            contador += 1
    return mayor

def menor(tupla):
    """
    A esta función se le provee una tupla para que obtenga el numero menor.
    """
    largo = len(tupla)
    contador = 0
    menor = int(tupla[0])
    while contador < largo:
        posicion = tupla[contador]
        if posicion < menor:
            menor = posicion
            contador += 1
        else:
            contador += 1
    return menor

def promedio(tupla):
    """
    A esta función se le provee una tupla para que obtenga
    el promedio de todos sus numeros.
    """
    largo = len(tupla)
    contador = 0
    promedio = 0
    while contador < largo:
        posicion = tupla[contador]
        promedio += posicion
        contador += 1
    promedio = promedio / largo
    return promedio

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    tupla = secuencia()
    print(f"Máximo: {mayor(tupla)} Mínimo: {menor(tupla)} Promedio: {promedio(tupla)}")


if __name__ == "__main__":
    principal()
