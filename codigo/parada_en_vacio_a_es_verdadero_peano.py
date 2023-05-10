"""parada_en_vacio_a_es_verdadero_peano.py

Implementa la reducción de _ParadaEnVacío_ a _EsVerdaderoPeano_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 5.1
"""

from es_verdadero_peano import es_verdadero_peano # oráculo
from parada_a_peano import parada_a_peano # NO es un oráculo

def parada_en_vacio_a_es_verdadero_peano(programa):
    para_en_peano = parada_a_peano(programa)
    return es_verdadero_peano(para_en_peano)