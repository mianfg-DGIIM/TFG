"""diagonal_a_universal.py

Implementa la reducción de _Diagonal_ a _Universal_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.8
"""

from universal import universal  # oráculo

def diagonal(programa):
    salida = universal(programa, programa)

    if salida == 'sí':
        return 'sí'
    else:
        return 'no'