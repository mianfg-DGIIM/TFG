"""adivina_consistente.py

Usado en la prueba la versión sintáctica del Primer Teorema de Incompletitud: de
ser el sistema lógico completo, este programa decidiría _AdivinaConsistente_

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 6.4
"""

import utilidades
from parada_a_S import parada_a_S # NO es un oráculo
from es_teorema_S import es_teorema_S # NO es un oráculo
from maquina_universal import maquina_universal # NO es un oráculo

def adivina_consistente(programa):
    programa_para = parada_a_S(programa)
    
    es_teorema = es_teorema_S(programa_para)

    if es_teorema == 'sí':
        salida = maquina_universal(programa, '')
        if salida == 'sí':
            return 'sí'
        else:
            return 'no'
    else:
        return 'no'