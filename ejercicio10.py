"""
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. funcion_a (a)
2. funcion_b (b)
3. funcion_c (c)
a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print(">>> Antes de la ejecución")
        resultado = funcion_b(*args, **kwargs)
        print(">>> Después de la ejecución")

        return resultado

    return funcion_c

@funcion_a
def suma(a, b):
    return a + b

print(suma(10, 20))