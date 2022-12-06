![Banner Python](images/Banner_Python.png)

# Decoradores en Python

Un decorador es una función que toma otra función de entrada y a su vez, devuelve por lo menos otra función.

---

**Sintaxis:**
  * **a(b) -> c**

---

**Ejemplo:**

```
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
```

---

**El resultado en al ejecutar este programa sería:**

```
>>> Antes de la ejecución
Hola desde una función
>>> Después de la ejecución
```