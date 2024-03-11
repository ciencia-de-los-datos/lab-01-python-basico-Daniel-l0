"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
def leer_archivo():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter="\t")
        data = list(reader)
    return data

def pregunta_01():
    data = leer_archivo()
    suma = sum([int(x[1]) for x in data])
    return suma
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
def pregunta_02():
    data = leer_archivo()
    count_dicc = {}
    for fila in data:
        letra = fila[0]
        count_dicc[letra] = count_dicc.get(letra, 0) + 1
    count_list = sorted(count_dicc.items())
    return count_list
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

def pregunta_03():
    data = leer_archivo()
    suma_dicc = {}
    for fila in data:
        letra = fila[0]
        suma = int(fila[1])
        suma_dicc[letra] = suma_dicc.get(letra, 0) + suma
    suma_list = sorted(suma_dicc.items())
    return suma_list
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

def pregunta_04():
    data = leer_archivo()
    month_count = {}
    for fila in data:
        fecha = fila[2]
        month = fecha.split('-')[1]
        month_count[month] = month_count.get(month, 0) + 1
    month_list = sorted(month_count.items())
    return month_list

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

def pregunta_05():
    data = leer_archivo()
    max_min_list = []
    for letra in 'ABCDE':
        max_val = max(int(fila[1]) for fila in data if fila[0] == letra)
        min_val = min(int(fila[1]) for fila in data if fila[0] == letra)
        max_min_list.append((letra, max_val, min_val))
    return max_min_list

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

def pregunta_06():
    data = leer_archivo()
    key_dict = {}
    for fila in data:
        dicc = fila[4].split(',')
        for item in dicc:
            key, val = item.split(':')
            if key not in key_dict:
                key_dict[key] = []
            key_dict[key].append(int(val))
    
    result = sorted([(key, min(values), max(values)) for key, values in key_dict.items()])
    return result
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """


def pregunta_07():
    data = leer_archivo()
    values_dict = {}
    for fila in data:
        value = int(fila[1])
        letra = fila[0]
        if value not in values_dict:
            values_dict[value] = []
        values_dict[value].append(letra)
    result = [(key, values) for key, values in sorted(values_dict.items())]
    return result
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """


def pregunta_08():
    data = leer_archivo()
    values_dict = {}
    for fila in data:
        value = int(fila[1])
        letra = fila[0]
        if value not in values_dict:
            values_dict[value] = set()
        values_dict[value].add(letra)
    result = [(key, sorted(list(values))) for key, values in sorted(values_dict.items())]
    return result

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

def pregunta_09():
    data = leer_archivo()
    count_dict = {}
    for fila in data:
        dicc = fila[4].split(',')
        for item in dicc:
            key, _ = item.split(':')
            count_dict[key] = count_dict.get(key, 0) + 1
    return dict(sorted(count_dict.items()))
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

def pregunta_10():
    data = leer_archivo()
    result = []
    for fila in data:
        letra = fila[0]
        num_col_4 = len(fila[3].split(','))
        num_col_5 = len(fila[4].split(','))
        result.append((letra, num_col_4, num_col_5))
    return result
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """


def pregunta_11():
    data = leer_archivo()
    sum_dict = {}
    for fila in data:
        letras = fila[3].split(',')
        suma = int(fila[1])
        for letra in letras:
            sum_dict[letra] = sum_dict.get(letra, 0) + suma
    return dict(sorted(sum_dict.items()))
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """


def pregunta_12():
    data = leer_archivo()
    sum_dict = {}
    for fila in data:
        letra = fila[0]
        suma = sum(int(val.split(':')[1]) for val in fila[4].split(','))
        sum_dict[letra] = sum_dict.get(letra, 0) + suma
    return dict(sorted(sum_dict.items()))
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """