"""
Decoradores con argumentos
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función
1. Función: plus_one (a)
2. Función: number (b)
3. Función:  (c)
a(b) -> c
"""

def plus_one(number):
    print("Executing plus_one")
    return number + 1

def function_call(function):
    print("Executing function_call")
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))