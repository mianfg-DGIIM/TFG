"""modifica_adivina_consistente.py

Usado para probar la no decidibilidad de _AdivinaConsistente_ (proposición 4.8)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.13
"""

import utilidades
from adivina_consistente import adivina_consistente # NO es un oráculo
from ignora_entrada import ignora_entrada

def modifica_adivina_consistente(programa):
    utilidades.escribir('disco/programa.txt', programa)
    utilidades.escribir('disco/entrada.txt', programa)

    salida = adivina_consistente(utilidades.leer('ignora_entrada.py'))

    if salida == 'sí':
        return 'no'
    elif salida == 'no':
        return 'sí'