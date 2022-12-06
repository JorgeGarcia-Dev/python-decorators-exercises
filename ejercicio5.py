"""
Un decorador es una función que recibe una función y regresa una función (al menos)
Lo utilizamos para extender funcionalidad de una función.

Función Saludar:

1. Función: saludador (a)
2. Función: saludado (b)
3. Función:  (c)
a(b) -> c

Función Admiración:

1. Función: admiracion (a)
2. Función: persona (b)
3. Función: envoltura (c)
a(b) -> c
"""

def saludador(saludado):
    return f"Hola {saludado}"

def admiracion(fn):

    def envoltura(persona):
        resultado = fn(persona)
        return f"¡¡¡ {resultado} !!!"

    return envoltura

saludador_animado = admiracion(saludador)

print(saludador_animado("Jorge"))

@admiracion
def despedidor(persona):
    return f"Adiós {persona}"

print(despedidor("Jorge"))