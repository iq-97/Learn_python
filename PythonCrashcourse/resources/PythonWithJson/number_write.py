# importar json
import json

number = [2, 3, 5, 6, 11, 13]

filename = 'numbers.json'

with open(filename, 'w')as f_object:
    # parametros en json: datos a almacenar, y el archivo donde se almacenara
    json.dump(number, f_object)