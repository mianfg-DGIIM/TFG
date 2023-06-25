"""godel_peano.py

Programa central de la demostración de la versión semántica Primer Teorema de
Incompletitud para ***Peano*** (teorema 6.1)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 6.1
"""

import utilidades

from es_teorema_peano import es_teorema_peano # NO es un oráculo
from parada_a_peano import parada_a_peano # NO es un oráculo

def godel_peano(entrada):
    programa_godel = utilidades.leer('godel_peano.py')
    para_en_peano = parada_a_peano(programa_godel)
    no_para_en_peano = 'NOT (' + para_en_peano + ')'

    if es_teorema_peano(no_para_en_peano) == 'sí':
        return 'para'
    else:
        utilidades.ciclar()