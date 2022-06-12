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
        if ord(caracter) + 1 == 123: # Si es z
            caracter = chr(96+ajuste)
        elif ord(caracter) + 1 == 58: # Si es 9
            caracter = chr(47+ajuste)
        elif ord(caracter) + 1 == 91: # Si es Z
            caracter = chr(64+ajuste)
        else: #Si es cualquier otro caracter
            caracter = chr(ord(caracter) + ajuste)
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
        caracter = chr(ord(caracter))
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
    contraseña = "bav10932"
    ajuste = 1
    cifrado= cifrar(contraseña, ajuste)
    print(f"Codificado: {cifrado}")
    decifrado= decifrar(contraseña, ajuste)
    print(f"Codificado: {decifrado}")


if __name__ == "__main__":
    principal()
