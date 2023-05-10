"""simula_turing.py

Este programa simula una máquina de Turing. Puedes usarlo con cualquiera de las
máquinas codificadas en la carpeta `maquinas_turing`

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 3.2
"""

import utilidades
from turing import Turing

def simula_turing(entrada):
    codificacion_maquina, entrada_maquina = utilidades.UAM(entrada)

    # creamos la máquina de Turing a partir de la entrada de la función SISO
    maquina_turing = Turing(codificacion_maquina, entrada_maquina)

    # ejecutamos la máquina
    maquina_turing.ejecutar()

    # si llegamos aquí, la máquina ha parado: devolvemos su configuración
    return str(maquina_turing)