"""maquina_universal.py

Implementa una máquina universal en Python, es decir, una función que acepta
como entradas un programa en Python y una entrada, y ejecuta el programa en
Python con dicha entrada

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.2
"""

import utilidades

def universal(programa, entrada):
    # esto define las funciones del programa, pero no las ejecuta
    try:
        exec(programa)
    except Exception as excepcion:
        return 'error: ' + str(excepcion)

    # extraemos una referencia a la función main, que está definida localmente
    main = utilidades.extraer_main(programa, locals())

    # invocamos la función
    return main(entrada)