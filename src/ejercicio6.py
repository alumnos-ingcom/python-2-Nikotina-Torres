################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El Cifrado del Cesar

El cifrado César o cifrado de rotación usa una encriptación de sustitución simple.
Esto significa que cada caracter se sustituye por otro caracter de acuerdo con un sistema especifico.

La codificación debe ser tal que la palabra codificada contenga unicamente caracteres del tipo AZaz y 0 a 9,
de manera que al codificar las ultimas letras del abecedario se vuelva a las primeras letras.
"""

def cifrar(palabra, ajuste):
    lista = []
    for i in palabra:
        lista.append(i)
    for l in range(len(lista)):
        caracter = lista[l]
        if ord(caracter) > 47 and ord(caracter) <= 56: #Si es 0-8
            caracter = chr(ord(caracter) + ajuste)
        elif ord(caracter) == 57: #Si es 9
            caracter = chr(47+ajuste)
        elif ord(caracter) > 64 and ord(caracter) <= 89: #Si es A-Y
            caracter = chr(ord(caracter) + ajuste)
        elif ord(caracter) == 90: #Si es Z
            caracter = chr(64+ajuste)
        elif ord(caracter) > 96 and ord(caracter) <= 121: #Si es a-y
            caracter = chr(ord(caracter)+ ajuste)
        elif ord(caracter) == 122: #Si es z
            caracter = chr(96+ajuste)
        lista[l] = caracter
    codificacion = ""
    for c in lista:
        codificacion += c
    return codificacion

def decifrar(palabra, ajuste):
    lista = []
    for i in palabra:
        lista.append(i)
    for l in range(len(lista)):
        caracter = lista[l]
        if ord(caracter) > 48 and ord(caracter) <= 57: #Si es 1-9
            caracter = chr(ord(caracter) - ajuste)
        elif ord(caracter) == 48: #Si es 0
            caracter = chr(58-ajuste)
        elif ord(caracter) > 65 and ord(caracter) <= 90: #Si es B-Z
            caracter = chr(ord(caracter) - ajuste)
        elif ord(caracter) == 65: #Si es A
            caracter = chr(91-ajuste)
        elif ord(caracter) > 97 and ord(caracter) <= 122: #Si es b-z
            caracter = chr(ord(caracter)- ajuste)
        elif ord(caracter) == 97: #Si es a
            caracter = chr(123-ajuste)
        lista[l] = caracter
    codificacion = ""
    for c in lista:
        codificacion += c
    return codificacion

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    contraseña = "az90AZ"
    ajuste = 1
    cifrado= cifrar(contraseña, ajuste)
    print(f"Codificado: {cifrado}")
    decifrado= decifrar(cifrado, ajuste)
    print(f"Decodificado: {decifrado}")


if __name__ == "__main__":
    principal()
