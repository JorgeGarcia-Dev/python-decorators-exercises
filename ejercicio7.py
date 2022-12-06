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

    def funcion_c(*args, **kwargs):

        print("Inicio del programa: ")
        funcion_b(*args, **kwargs)
        print("Fin del programa.")

    return funcion_c

@funcion_a
def suma(num_1, num_2, num_3):
    print(num_1 + num_2 + num_3)

@funcion_a
def resta(num_1, num_2):
    print(num_1 - num_2)

def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 10)
resta(30, 10)
potencia(base=5, exponente=3)