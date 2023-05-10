"""godel.py

Programa central de la demostración del Primer Teorema de Incompletitud

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 6.1
"""

import utilidades

from es_teorema_peano import es_teorema_peano # NO es un oráculo
from parada_a_peano import parada_a_peano # NO es un oráculo

def godel(entrada):
    programa_godel = utilidades.leer('godel.py')
    para_en_peano = parada_a_peano(programa_godel)
    no_para_en_peano = 'NOT (' + para_en_peano + ')'

    if es_teorema_peano(no_para_en_peano) == 'sí':
        return 'para'
    else:
        utilidades.ciclar()