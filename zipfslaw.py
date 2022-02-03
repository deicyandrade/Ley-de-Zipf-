
import collections


def generate_zipf_table(text, top):

    """
    Crea una lista de diccionarios que contienen las
    palabras más frecuentes, sus frecuencias y
    otros datos de Zipfian
    """
    
    text = _remove_punctuation(text)
    text = text.lower()
    top_word_frequencies = _top_word_frequencies(text, top)
    zipf_table = _create_zipf_table(top_word_frequencies)
    return zipf_table


def _remove_punctuation(text):

    """
   Elimina los caracteres:
    !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789
    from the text.
    """

    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

    tr = str.maketrans("", "", chars_to_remove)

    return text.translate(tr)


def _top_word_frequencies(text, top):

    """
    Crea una lista de tuplas que contienen las
    palabras más frecuentes y sus frecuencias
    en orden descendente.
    """

    # Sin argumentos, split() separa la cadena
    # por 1 o más espacios en blanco consecutivos.
    words = text.split()

    #Crear una instancia de colecciones.Contador a partir de un
    # iterable, en este caso nuestra lista de palabras.
    word_frequencies = collections.Counter(words)

    # most_common() nos da una lista de tuplas
    # que contienen palabras y sus frecuencias,
    # en orden descendente de frecuencia.
    top_word_frequencies = word_frequencies.most_common(top)

    return top_word_frequencies


def _create_zipf_table(frequencies):

    """
    Toma la lista creada por _top_word_frequencies
    y la inserta en una lista de diccionarios,
    junto con los datos de Zipfian.
    """

    zipf_table = []

    top_frequency = frequencies[0][1]

    for index, item in enumerate(frequencies, start=1):

        relative_frequency = "1/{}".format(index)
        zipf_frequency = top_frequency * (1 / index)
        difference_actual = item[1] - zipf_frequency
        difference_percent = (item[1] / zipf_frequency) * 100

        zipf_table.append({"Palabra": item[0],
                           "Frecuencia_actual": item[1],
                           "Frecuencia relativa": relative_frequency,
                           "Frecuencia_zipf": zipf_frequency,
                           "Diferencia_actual": difference_actual,
                           "Diferencia_porcentaje": difference_percent})

    return zipf_table


def print_zipf_table(zipf_table):

    """
    Imprime la lista creada por generate_zipf_table en formato de tabla con encabezados de columna.
    """

    width = 80

    print("-" * width)
    print("|Rango|    Palabra | Frecuencia actual | Fractura Zipf | Frec Zipf |Dif. actual |Dif. porcentaje|")
    print("-" * width)

    format_string = "|{:4}|{:12}|{:12.0f}|{:>12}|{:12.2f}|{:12.2f}|{:7.2f}%|"

    for index, item in enumerate(zipf_table, start=1):

        print(format_string.format(index,
                                   item["palabra"],
                                   item["frecuencia_actual"],
                                   item["Frecuencia_actual"],
                                   item["Frecuencia_zipf"],
                                   item["Diferencia_actual"],
                                   item["Diferencia_porcentaje"]))

    print("-" * width)

