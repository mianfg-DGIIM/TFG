"""utilidades.py

Este programa implementa funciones que se usan en el resto de programas
("utilidades")

---
Autor: Miguel Ángel Fernández Gutiérrez
"""

import re
from string import printable
from inspect import signature


# para identificar las excepciones que levantamos intencionadamente
class ExcepcionTFG(Exception):
    pass


def leer_archivo(ruta):
    archivo = ''
    with open(ruta) as entrada:
        archivo = entrada.read()
    return archivo

def escribir_archivo(ruta, contenidos):
    with open(ruta, 'w') as f:
        f.write(contenidos)

# para abreviar
leer = leer_archivo
escribir = escribir_archivo


def MAU(*entradas, SEP='::'):
    return SEP.join(entradas)

def UAM(entrada, SEP='::'):
    return entrada.split(SEP)


def en_alfabeto(palabra, alfabeto):
    regex = rf"^({'|'.join(alfabeto)})*$"
    return bool(re.search(regex, palabra))


def extraer_nombre_main(programa):
    main_regex = r'^def\s+([a-zA-Z0-9_]*)'
    buscar_main = re.search(main_regex, programa, re.MULTILINE)
    
    if buscar_main:
        return buscar_main.group(1)
    else:
        # no hay función main definida
        # nunca debería pasar en un programa SISO
        return None

def extraer_main(programa, variables_locales):
    nombre_main = extraer_nombre_main(programa)
    print("WIP nombre main:", nombre_main)

    if not nombre_main:
        # no hay una función main definida
        return lambda _: 'error: no hay una función main definida'

    if nombre_main in variables_locales:
        main = variables_locales[nombre_main]

        # comprobamos si la función main acepta un único parámetro
        num_paremeters = len(signature(main).parameters)
        if num_paremeters == 1:
            return main
        else:
            return lambda _: f"error: función '{nombre_main}' no es SISO, pues admite {num_paremeters} parámetros"
    else:
        # la función no está definida localmente
        return lambda _: f"error: función '{nombre_main}' no definida localmente"

# asumimos como el alfabeto de Python a los caracteres de string.printable
# (por simplicidad, no pondremos todos los caracteres UTF-8)
ALFABETO_PYTHON = list(str(printable))

def siguiente_string(string, alfabeto=ALFABETO_PYTHON):
    primero = alfabeto[0]
    ultimo = alfabeto[-1]
    if string == '':
        return str(primero)
    caracteres = [c for c in string]
    longitud = len(caracteres)

    # la variable booleana desborda indicará si este es el último
    # string de longitud actual
    desborda = True
    i = None # para mantener el valor de i
    for i in range(longitud-1, -1, -1):
        caracter_actual = caracteres[i]
        if caracter_actual != ultimo:
            desborda =  False
            break
    # podemos desbordar (y es i == 0) o no, en cuyo caso el valor
    # de i es el índice del caracter más a la derecha que puede ser
    # incrementado - especificamos a continuación toda la información
    # que necesitamos sobre ese caracter
    incremento_i = i
    alfabeto_i = alfabeto.index(caracter_actual)

    if desborda:
        # devolvemos el siguiente caracter, que es el primer caracter
        # repetido longitud + 1 veces
        return primero*(longitud+1)
    else:
        # no hemos desbordado: manipulamos la lista de caracteres para
        # producir el siguiente caracter en order lexicográfico
        
        # el caracter más a la derecha que puede ser incrementado es
        # incrementado
        caracteres[incremento_i] = alfabeto[alfabeto_i+1]

        # a continuación todos los caracteres a la derecha de éste
        # se transforman en el primer caracter del alfabeto
        for j in range(incremento_i+1, longitud):
            caracteres[j] = primero
        return ''.join(caracteres)

def ciclar():
    while True:
        pass
