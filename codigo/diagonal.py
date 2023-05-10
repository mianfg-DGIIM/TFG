"""diagonal.py

Si _Universal_ fuese decidible, este programa decidiría el problema _Diagonal_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.5
"""

from universal import universal

def diagonal(programa):
    return universal(programa, programa)