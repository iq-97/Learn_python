def count_words(filename):
    """cuenta el numero aproximado de palabras que aparecen en un documento"""
    try:
        with open(filename) as f_object:
            contenido = f_object.read()
    except FileNotFoundError:
        msg = "no existe el archivo especificado"
        print(msg)
    else:
        # cuenta el aproximo de numero de palabras que hay en el texto
        words = contenido.split()
        count_words = len(words)
        print("el aproximado de numero de palabras que hay en el archivo"+filename+" es de: "+str(count_words))