"""
Decoradores con argumentos
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. funcion_decorador_a (a)
2. funcion_a_decorar_b (b)
3. funcion_decorada_c (c)
a(b) -> c
"""

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes desde la función_decorada_c')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después desde la función decorada_c')
        return resultado

    return funcion_decorada_c


@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(5, 6)
print(f'Resultado suma: {resultado}')