"""c_diagonal.py

Si _Diagonal_ fuese decidible, este programa decidiría el problema _C-Diagonal_
(proposición 4.3)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.6
"""

from diagonal import diagonal

def c_diagonal(programa):
    salida = diagonal(programa)

    if salida == 'sí':
        return 'no'
    else:
        return 'sí'