"""
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función.
1. funcion_a (a)
2. funcion_b (b)
3. funcion_c (c)
a(b) -> c
"""

# En este ejemplo, en la "funcion_a", recibimos a la "funcion_b" que proviene de la funcion "saludar", y que retornará
# lo que se encuentre dentro de la "funcion_c".
def funcion_a(funcion_b):

    def funcion_c():
        print(">>> Antes de la ejecución")
        funcion_b()
        print(">>> Después de la ejecución \n")

    return funcion_c

@funcion_a
def saludar():
    print("Hola desde una función")

saludar()

# La salida en terminal sería:

"""
>>> Antes de la ejecución
Hola desde una función
>>> Después de la ejecución
"""