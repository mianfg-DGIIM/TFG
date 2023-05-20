"""godel.py

Programa central de la demostración de la versión semántica Primer Teorema de
Incompletitud (en el caso general)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 6.2
"""

import utilidades

from es_teorema_en_G import es_teorema_en_G # NO es un oráculo
from parada_a_G import parada_a_G # NO es un oráculo

def incompleto_semantico(entrada):
    programa = utilidades.leer('incompleto_semantico.py')
    para_en_G = parada_a_G(programa)
    no_para_en_G = 'NOT (' + para_en_G + ')'

    if es_teorema_en_G(no_para_en_G) == 'sí':
        return 'para'
    else:
        utilidades.ciclar()