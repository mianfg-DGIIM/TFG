"""ignora_entrada.py

Permite ignorar la entrada y ejecutar programas y entradas almacenados en disco

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 4.11
"""

import utilidades
from maquina_universal import maquina_universal

def ignora_entrada(entrada_ignorada):
    programa = utilidades.leer('disco/programa.txt')
    entrada = utilidades.leer('disco/entrada.txt')
    return maquina_universal(programa, entrada)