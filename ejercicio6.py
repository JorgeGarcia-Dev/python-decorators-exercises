"""
Decoradores con argumentos
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. funcion__a (a)
2. funcion_b (b)
3. funcion_c (c)
a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():

        print("Inicio del programa: ")
        funcion_b()
        print("Fin del programa.")

    return funcion_c

@funcion_a
def suma():
    print(15 + 20)

@funcion_a
def resta():
    print(50 - 25)

suma()
resta()