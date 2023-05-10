"""simula_turing_decision.py

Este programa es una variación de `simula_turing.py` para hacer que el programa
sea de decisión (siempre se devuelve 'sí' o 'no'). Este programa no se usa en el
trabajo, pero se deja aquí para permitir la experimentación

---
Autor: Miguel Ángel Fernández Gutiérrez
"""

import utilidades
from turing import Turing

def decision_turing(entrada):
    codificacion_maquina, entrada_maquina = utilidades.UAM(entrada)

    # creamos la máquina de Turing a partir de la entrada de la función SISO
    maquina_turing = Turing(codificacion_maquina, entrada_maquina)

    # ejecutamos la máquina
    maquina_turing.ejecutar()

    # si llegamos aquí, la máquina ha parado
    # devolvemos si la entrada es aceptada o rechazada
    return maquina_turing.acepta_o_rechaza()