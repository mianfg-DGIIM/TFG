"""universal_a_parada_en_vacio.py

Implementa la reducción de _Universal_ a _ParadaEnVacío_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.11
"""

import utilidades
from parada_en_vacio import parada_en_vacio # oráculo

def universal_a_parada_en_vacio(programa):
    maquina_universal_parada = utilidades.leer('maquina_universal_parada.py')

    return parada_en_vacio(maquina_universal_parada, utilidades.MAU(programa, ''))