"""c_d.py

Usado para probar que si un programa es decidible, su complementario también
(proposición 4.4)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.7
"""

from d import d

def c_d(entrada):
    salida = d(entrada)

    if salida == 'sí':
        return 'no'
    else:
        return 'sí'