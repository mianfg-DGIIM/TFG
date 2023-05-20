# Código

En esta carpeta del repositorio se encuentran los programas que han sido redactados en la memoria.

## Lista de programas

| Programa | En la memoria | Descripción | ¿Puede ejecutarse?* |
| --- | --- | --- | --- |
| [`adivina_consistente.py`](./adivina_consistente.py) | Programa 6.4 | Usado en la prueba la versión sintáctica del Primer Teorema de Incompletitud: de ser el sistema lógico completo, este programa decidiría _AdivinaConsistente_ | ❌ |
| [`c_d.py`](./c_d.py) | Programa 4.7 | Usado para probar que si un programa es decidible, su complementario también | ❌ |
| [`c_diagonal.py`](./c_diagonal.py) | Programa 4.6 | Si _Diagonal_ fuese decidible, este programa decidiría el problema _C-Diagonal_ | ✅ |
| [`diagonal.py`](./diagonal.py) | Programa 4.5 | Si _Universal_ fuese decidible, este programa decidiría el problema _Diagonal_ | ✅ |
| [`diagonal_a_universal.py`](./diagonal_a_universal.py) | Programa 4.8 | Implementa la reducción de _Diagonal_ a _Universal_ | ✅ |
| `es_prueba_peano.py` |  | Este programa es capaz de comprobar si una secuencia de fórmulas es una prueba de otra cierta fórmula en ***Peano*** | ⭕️ |
| [`es_teorema_peano.py`](./es_teorema_peano.py) | Programa 5.2 | Este programa hace _EsTeoremaPeano_ semidecidible | ❌ |
| [`es_teorema_S.py`](./es_teorema_S.py) | Programa 6.3 | Prueba que _EsTeorema_ es decidible para sistemas lógicos sintácticamente consistentes | ❌ |
| [`funcion_con_objeto_codificado.py`](./funcion_con_objeto_codificado.py) | Programa 3.1 | Este programa muestra que los programas SISO no imponen una restricción sobre los programas que podemos escribir: podemos aceptar como entrada y devolver como salida cualquier programa debidamente codificado (en este caso, mediante la librería nativa `pickle`) | ✅ |
| [`godel.py`](./godel.py) | Programa 6.2 | Programa central de la demostración de la versión semántica Primer Teorema de Incompletitud (en el caso general) | ❌ |
| [`godel_peano.py`](./godel_peano.py) | Programa 6.1 | Programa central de la demostración de la versión semántica Primer Teorema de Incompletitud (en el caso de ***Peano***) | ❌ |
| [`ignora_entrada.py`](./ignora_entrada.py) | Programa 4.11 | Permite ignorar la entrada y ejecutar programas y entradas almacenados en disco | ✅ |
| [`maquina_universal.py`](./maquina_universal.py) | Programa 4.2 | Implementa una máquina universal en Python, es decir, una función que acepta como entradas un programa en Python y una entrada, y ejecuta el programa en Python con dicha entrada | ✅ |
| [`maquina_universal_parada.py`](./maquina_universal_parada.py) | Programa 4.9 | Programa usado como parte de la reducción de _Universal_ a _Parada_ y de _Universal_ a _ParadaEnVacío_ | ✅ |
| [`mas_a_que_b.py`](./mas_a_que_b.py) | Programa 4.1 | Este programa decide el problema _MásAQueB_ | ✅ |
| [`mas_a_que_b_v2.py`](./mas_a_que_b_v2.py) | Programa 4.3 | Este programa decide el problema _MásAQueB_, aceptando cualquier palabra como entrada (tiene todos los caracteres en el alfabeto) | ✅ |
| [`modifica_adivina_consistente.py`](./modifica_adivina_consistente.py) | Programa 4.13 | Usado para probar la no decidibilidad de _AdivinaConsistente_ | ❌ |
| [`parada_a_parada_en_vacio.py`](./parada_a_parada_en_vacio.py) | Programa 4.12 | Implementa la reducción de _Parada_ a _ParadaEnVacío_ | ❌ |
| `parada_a_peano.py` |  | Este programa traduce una afirmación del tipo _"P para con entrada vacía"_ a una fórmula de ***Peano*** | ⭕️ |
| [`parada_en_vacio_a_es_verdadero_peano.py`](./parada_en_vacio_a_es_verdadero_peano.py) | Programa 5.1 | Implementa la reducción de _ParadaEnVacío_ a _EsVerdaderoPeano_ | ❌ |
| [`si.py`](./si.py) | Programa 4.4 | Este programa decide el problema _Sí_ | ✅ |
| [`simula_turing.py`](./simula_turing.py) | Programa 3.2 | Este programa simula una máquina de Turing. Puedes usarlo con cualquiera de las máquinas codificadas en la carpeta [`maquinas_turing`](./maquinas_turing) | ✅ |
| [`simula_turing_decision.py`](./simula_turing_decision.py) |  | Este programa es una variación de [`simula_turing.py`](./simula_turing.py) para hacer que el programa sea de decisión (siempre se devuelve 'sí' o 'no'). Este programa no se usa en el trabajo, pero se deja aquí para permitir la experimentación | ✅ |
| [`suma_binaria.py`](./suma_binaria.py) |  | Este programa decide los problemas _EsTeorema_ y _EsVerdadero_ para todos los sistemas lógicos derivados del sistema formal ***SumaBinaria*** (incluyendo la decidibilidad del problema _EsTeorema_ de este sistema formal) | ✅ |
| [`turing.py`](./turing.py) |  | Este programa incluye una clase `Turing` que encapsula la simulación de [`simula_turing.py`](./simula_turing.py) | ✅ |
| [`universal.py`](./universal.py) |  | Este programa hace el problema _Universal_ semidecidible. Esto no es probado en el trabajo, pero se deja aquí para permitir la experimentación con el problema | ✅ |
| [`universal_a_parada.py`](./universal_a_parada.py) | Programa 4.10 | Implementa la reducción de _Universal_ a _Parada_ | ❌ |
| [`utilidades.py`](./utilidades.py) |  | Este programa implementa funciones que se usan en el resto de programas ("utilidades") | ✅ |

> \* ✅ = "sí", ❌ = "no", ⭕️ = "no implementado"
> 
> Con "¿puede ejecutarse?" nos preguntamos a si podemos ejecutar los programas en el intérprete de Python, no si los programas son o no decidibles/semidecidibles. Tienes más información sobre por qué los programas no pueden ejecutarse [más adelante](#una-advertencia).

## Cómo usar el código

Puedes ejecutar los programas de la carpeta codigo importando las funciones que quieras en el intérprete de Python. En la librería `utilidades.py` aparecen múltiples funciones que se usan en varios programas, y que son útiles para poder ejecutar otros. A modo de ejemplo, si queremos ejecutar la función `simula_turing_mult` de `simula_turing.py`, haremos:

```
TFG/codigo$ python
>>> from utilidades import leer
>>> from simula_turing import simula_turing_mult
>>> codificacion = leer('./maquinas_turing/mas_a_que_b.mt')
>>> entrada = 'abaaabbb'
>>> simula_turing_mult(codificacion, entrada)
'q_0 : X X X X X X X X [_] (rechaza)
```

## Una advertencia

Algunos de los programas no se pueden ejecutar, en concreto:

| Programa no ejecutable | Motivo |
| --- | --- |
| [`adivina_consistente.py`](./adivina_consistente.py) | Las funciones `parada_a_S` y `es_prueba_S` no están implementadas (es un sistema lógico cualquiera), pero su existencia se prueba |
| [`c_d.py`](./c_d.py) | La función `d` no existe (este programa es ilustrativo). Prueba a sustituir `d` por cualquier otro programa de decisión |
| [`es_teorema_peano.py`](./es_teorema_peano.py) | La función `es_prueba_peano` no está implementada (sería un trabajo muy arduo), pero su existencia se prueba |
| [`godel.py`](./godel.py) | Las funciones `es_teorema_en_G` y `parada_a_G` no están implementadas (es un sistema lógico cualquiera), pero su existencia se prueba |
| [`godel_peano.py`](./godel_peano.py) | La función `parada_a_peano` no está implementada (sería un trabajo muy arduo), pero su existencia se prueba |
| [`modifica_adivina_consistente.py`](./modifica_adivina_consistente.py) | No puede escribirse dado que _AdivinaConsistente_ es no decidible (y no está implementado) |
| [`parada_a_parada_en_vacio.py`](./parada_a_parada_en_vacio.py) | Es una reducción en la que `parada_en_vacio` es un oráculo |
| [`parada_en_vacio_a_es_verdadero_peano.py`](./parada_en_vacio_a_es_verdadero_peano.py) | Es una reducción en la que `es_verdadero_peano` es un oráculo, y donde `parada_a_peano` no está implementada (ya hemos explicado el por qué), pero NO es un oráculo (su existencia se prueba) |
| [`universal_a_parada.py`](./universal_a_parada.py) | Es una reducción en la que `parada` es un oráculo (de hecho no está implementada porque no es computable) |
