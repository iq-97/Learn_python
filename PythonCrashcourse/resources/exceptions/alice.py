# ejemplo de excepciones de archivos

import count_words as mod_words

# analizando texto
filenames = ['alice.txt', 'uno.txt', 'luck_of_dudley.txt', 'dato.txt']

for filename in filenames:
    mod_words.count_words(filename)

