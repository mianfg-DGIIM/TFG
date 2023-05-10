"""universal_a_parada.py

Implementa la reducción de _Universal_ a _Parada_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.10
"""

import utilidades
from parada import parada # oráculo

def universal_a_parada(programa, entrada):
    entrada_codificada = utilidades.MAU(programa, entrada)
    maquina_universal_parada = utilidades.leer('maquina_universal_parada.py')

    return parada(maquina_universal_parada, entrada_codificada)