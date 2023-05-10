"""universal.py

Este programa hace el problema _Universal_ semidecidible. Esto no es probado en
el trabajo, pero se deja aquí para permitir la experimentación con el problema

---
Autor: Miguel Ángel Fernández Gutiérrez
"""

from maquina_universal import maquina_universal

def universal_decision(programa, entrada):
    salida = maquina_universal(programa, entrada)

    if salida == 'sí':
        return 'sí'
    else:
        return 'no'