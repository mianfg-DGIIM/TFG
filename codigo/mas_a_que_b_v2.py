"""mas_a_que_b_v2.py

Este programa decide el problema _MásAQueB_, aceptando cualquier palabra
como entrada (tiene todos los caracteres en el alfabeto)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.3
"""

def mas_a_que_b_v2(palabra):
    # aceptamos cualquier palabra del alfabeto UTF-8

    if palabra.count('a') > palabra.count('b'):
        return 'sí'

    return 'no'