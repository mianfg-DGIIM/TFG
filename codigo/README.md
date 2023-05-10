# Código

En esta carpeta del repositorio se encuentran los programas que han sido redactados en la memoria.

## Lista de programas

| Programa | En la memoria | Descripción | ¿Puede ejecutarse?* |
| --- | --- | --- | --- |
| [`c_d.py`](./c_d.py) | Programa 4.7 | Usado para probar que si un programa es decidible, su complementario también | ❌ |
| [`c_diagonal.py`](./c_diagonal.py) | Programa 4.6 | Si _Diagonal_ fuese decidible, este programa decidiría el problema _C-Diagonal_ | ✅ |
| [`diagonal.py`](./diagonal.py) | Programa 4.5 | Si _Universal_ fuese decidible, este programa decidiría el problema _Diagonal_ | ✅ |
| [`diagonal_a_universal.py`](./diagonal_a_universal.py) | Programa 4.8 | Implementa la reducción de _Diagonal_ a _Universal_ | ✅ |
| `es_prueba_peano.py` |  | Este programa es capaz de comprobar si una secuencia de fórmulas es una prueba de otra cierta fórmula en ***Peano*** | NO IMPLEMENTADO |
| [`es_teorema_peano.py`](./es_teorema_peano.py) | Programa 5.2 | Este programa hace _EsTeoremaPeano_ semidecidible | ❌ |
| [`funcion_con_objeto_codificado.py`](./funcion_con_objeto_codificado.py) | Programa 3.1 | Este programa muestra que los programas SISO no imponen una restricción sobre los programas que podemos escribir: podemos aceptar como entrada y devolver como salida cualquier programa debidamente codificado (en este caso, mediante la librería nativa `pickle`) | ✅ |
| [`godel.py`](./godel.py) | Programa 6.1 | Programa central de la demostración del Primer Teorema de Incompletitud | ❌ |
| [`maquina_universal.py`](./maquina_universal.py) | Programa 4.2 | Implementa una máquina universal en Python, es decir, una función que acepta como entradas un programa en Python y una entrada, y ejecuta el programa en Python con dicha entrada | ✅ |
| [`maquina_universal_parada.py`](./maquina_universal_parada.py) | Programa 4.9 | Programa usado como parte de la reducción de _Universal_ a _Parada_ y de _Universal_ a _ParadaEnVacío_ | ✅ |
| [`mas_a_que_b.py`](./mas_a_que_b.py) | Programa 4.1 | Este programa decide el problema _MásAQueB_ | ✅ |
| [`mas_a_que_b_v2.py`](./mas_a_que_b_v2.py) | Programa 4.3 | Este programa decide el problema _MásAQueB_, aceptando cualquier palabra como entrada (tiene todos los caracteres en el alfabeto) | ✅ |
| `parada_a_peano.py` |  | Este programa traduce una afirmación del tipo _"P para con entrada vacía"_ a una fórmula de ***Peano*** | NO IMPLEMENTADO |
| [`parada_en_vacio_a_es_verdadero_peano.py`](./parada_en_vacio_a_es_verdadero_peano.py) | Programa 5.1 | Implementa la reducción de _ParadaEnVacío_ a _EsVerdaderoPeano_ | ❌ |
| [`si.py`](./si.py) | Programa 4.4 | Este programa decide el problema _Sí_ | ✅ |
| [`simula_turing.py`](./simula_turing.py) | Programa 3.2 | Este programa simula una máquina de Turing. Puedes usarlo con cualquiera de las máquinas codificadas en la carpeta [`maquinas_turing`](./maquinas_turing) | ✅ |
| [`simula_turing_decision.py`](./simula_turing_decision.py) |  | Este programa es una variación de [`simula_turing.py`](./simula_turing.py) para hacer que el programa sea de decisión (siempre se devuelve 'sí' o 'no'). Este programa no se usa en el trabajo, pero se deja aquí para permitir la experimentación | ✅ |
| [`suma_binaria.py`](./suma_binaria.py) |  | Este programa decide los problemas _EsTeorema_ y _EsVerdadero_ para todos los sistemas lógicos derivados del sistema formal ***SumaBinaria*** (incluyendo la decidibilidad del problema _EsTeorema_ de este sistema formal) | ✅ |
| [`turing.py`](./turing.py) |  | Este programa incluye una clase `Turing` que encapsula la simulación de [`simula_turing.py`](./simula_turing.py) | ✅ |
| [`universal.py`](./universal.py) |  | Este programa hace el problema _Universal_ semidecidible. Esto no es probado en el trabajo, pero se deja aquí para permitir la experimentación con el problema | ✅ |
| [`universal_a_parada.py`](./universal_a_parada.py) | Programa 4.10 | Implementa la reducción de _Universal_ a _Parada_ | ❌ |
| [`universal_a_parada_en_vacio.py`](./universal_a_parada_en_vacio.py) | Programa 4.11 | Implementa la reducción de _Universal_ a _ParadaEnVacío_ | ❌ |
| [`utilidades.py`](./utilidades.py) |  | Este programa implementa funciones que se usan en el resto de programas ("utilidades") | ✅ |

> *Con "¿puede ejecutarse?" nos preguntamos a si podemos ejecutar los programas en el intérprete de Python, no si los programas son o no decidibles/semidecidibles. Tienes más información sobre por qué los programas no pueden ejecutarse [más adelante](#una-advertencia).

## Cómo usar el código

Puedes encontrar más información sobre cómo usar los programas de esta carpeta en la memoria (**apéndice A**).

## Una advertencia

Algunos de los programas no se pueden ejecutar, en concreto:

| Programa no ejecutable | Motivo |
| --- | --- |
| [`c_d.py`](./c_d.py) | La función `d` no existe (este programa es ilustrativo). Prueba a sustituir `d` por cualquier otro programa de decisión |
| [`es_teorema_peano.py`](./es_teorema_peano.py) | La función `es_prueba_peano` no está implementada (sería un trabajo muy arduo). Su existencia se prueba en **WIP** |
| [`godel.py`](./godel.py) | La función `parada_a_peano` no está implementada (sería un trabajo muy arduo). Su existencia se prueba en **WIP** |
| [`parada_en_vacio_a_es_verdadero_peano.py`](./parada_en_vacio_a_es_verdadero_peano.py) | Es una reducción en la que `es_verdadero_peano` es un oráculo, y donde `parada_a_peano` no está implementada (ya hemos explicado el por qué), pero NO es un oráculo (su existencia se prueba en **WIP**) |
| [`universal_a_parada.py`](./universal_a_parada.py) | Es una reducción en la que `parada` es un oráculo (de hecho no está implementada porque no es computable) |
| [`universal_a_parada_en_vacio.py`](./universal_a_parada_en_vacio.py) | Es una reducción en la que `parada_en_vacio` es un oráculo (de hecho no está implementada porque no es computable) |
