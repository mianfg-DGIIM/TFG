"""mas_a_que_b.py

Este programa decide el problema _MásAQueB_ (proposición 4.1)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.1
"""

import utilidades

def mas_a_que_b(palabra):
    # comprobamos si la codificación es correcta, es decir (si es del alfabeto {'a', 'b'}), si no es correcta devolvemos 'no'
    if not utilidades.en_alfabeto(palabra, {'a', 'b'}):
        return 'no'

    if palabra.count('a') > palabra.count('b'):
        return 'sí'

    return 'no'