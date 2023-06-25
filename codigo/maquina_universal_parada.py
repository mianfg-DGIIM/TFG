"""maquina_universal_parada.py

Programa usado para demostrar que _Parada_ no es decidible (proposición 4.6)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.9
"""

import utilidades
from maquina_universal import maquina_universal

def maquina_universal_parada(entrada_codificada):
    (programa, entrada) = utilidades.UAM(entrada_codificada)
    salida = maquina_universal(programa, entrada)

    if salida == 'sí':
        return 'sí'
    else:
        utilidades.ciclar()