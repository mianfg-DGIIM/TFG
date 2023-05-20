"""es_teorema_S.py

Prueba que _EsTeorema_ es decidible para sistemas lógicos sintácticamente
consistentes

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 6.3
"""

import utilidades
from es_prueba_S import es_prueba_S # NO es un oráculo

def es_teorema_S(formula):
    negacion_formula = 'NOT (' + formula + ')'
    demostracion = ''

    while True:
        if es_prueba_S(demostracion, formula) == 'sí':
            return 'sí'
        if es_prueba_S(demostracion, negacion_formula) == 'sí':
            return 'no'
        demostracion = utilidades.siguiente_string(demostracion)