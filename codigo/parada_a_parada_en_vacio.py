"""parada_a_parada_en_vacio.py

Implementa la reducción de _Parada_ a _ParadaEnVacío_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.12
"""

import utilidades
from parada_en_vacio import parada_en_vacio # oráculo

def parada_a_parada_en_vacio(programa, entrada):
    utilidades.escribir('disco/programa.txt', programa)
    utilidades.escribir('disco/entrada.txt', entrada)

    return parada_en_vacio(utilidades.leer('ignora_entrada.py'))