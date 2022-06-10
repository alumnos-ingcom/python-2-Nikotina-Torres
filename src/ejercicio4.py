################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci

 La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores.
 En la misma, los dos primeros términos son 1.
 (En algunos lugares se toma el primer término en 0 y el segundo en 1)
 Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci.
 Siendo este número un entero positivo mayor a 2.
"""

def fibonacci(numero):
    a=1
    b=1
    c=3
    if numero == 0 or numero == 1:
        return a
    else:
        for _ in range(numero):
            total=a+b
            b=a
            a=total
            c+=1
        return total

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = 13
    print(fibonacci(numero))


if __name__ == "__main__":
    principal()
