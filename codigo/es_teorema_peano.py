"""es_teorema_peano.py

Este programa hace _EsTeoremaPeano_ semidecidible (proposición 5.8)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 5.2
"""

import utilidades
from es_prueba_peano import es_prueba_peano # NO es un oráculo

def es_teorema_peano(fórmula):
    demostración = ''

    while True:
        if es_prueba_peano(demostración, fórmula) == 'sí':
            return 'sí'
        demostración = utilidades.siguiente_string(demostración)