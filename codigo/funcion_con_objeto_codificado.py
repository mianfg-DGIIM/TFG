"""funcion_con_objeto_codificado.py

Este programa muestra que los programas SISO no imponen una restricción sobre
los programas que podemos escribir: podemos aceptar como entrada y devolver
como salida cualquier programa debidamente codificado (en este caso, mediante
la librería nativa `pickle`)

---
Autor: Miguel Ángel Fernández Gutiérrez
En la memoria: Programa 3.1
"""

import pickle

def función_con_objeto_codificado(codificado):
    descodificado = pickle.loads(codificado)
    # realizamos las operaciones que queramos con el objeto descodificado
    # el objeto descodificado puede ser de cualquier tipo

# creamos un objeto, or ejemplo, una matriz
adyacencias = {1:2, 3:4, 5:3, 4:2}

# serializamos (codificamos) el objeto a un string
adyacencias_codificado = pickle.dumps(adyacencias)

# podemos ahora ejecutar este objeto dentro de una función SISO
función_con_objeto_codificado(adyacencias_codificado)
