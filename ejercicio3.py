"""
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. Función: decorador (a)
2. Función: suma (b)
3. Función: wrapper (c)
a(b) -> c
"""

def decorador(suma):

    def wrapper():
        print("Mensaje de entrada.")
        print(suma())
        print("Mensaje de salida.")
        return suma

    return wrapper

@decorador
def suma():
    suma = 10 + 50
    return "El resultado de la suma es: ", suma

suma()