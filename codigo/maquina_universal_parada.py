"""maquina_universal_parada.py

Programa usado como parte de la reducción de _Universal_ a _Parada_ y de
_Universal_ a _ParadaEnVacío_

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
        return 'para'
    else:
        utilidades.ciclar()