"""
Decoradores con argumentos
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función.

Función Saludar:

1. Función: calcular_tiempo (a)
2. Función: name (b)
3. Función: wrapper (c)
4. Función: wrapper_2 (d)
a(b) -> c
"""

import time

def calcular_tiempo(suma):

    def wrapper(function):

        def wrapper_2(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)

            print(f"El tiempo total para la función {suma} es dé: ", time.time() - start)

            return result

        return wrapper_2

    return wrapper

@calcular_tiempo('suma')
def suma(a, b):
    time.sleep(2)
    return a + b

print(suma(10, 20))