"""
Decoradores con argumentos
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. Función: my_custome_decorator (a)
2. Función: function (b)
3. Función: wrapper (c)
a(b) -> c
"""

def my_custome_decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper

@my_custome_decorator
def saludar():
    print("Hola desde una función")

@my_custome_decorator
def suma(a, b):
    return a + b