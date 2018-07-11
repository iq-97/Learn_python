# A example to import of estandard library
# importando modulo para trabajar con ordenamiento de diccionarios
from collections import OrderedDict
# Orderdict crea un diccionario vacio
favorite_languajes = OrderedDict()

favorite_languajes['jen'] = 'python'
favorite_languajes['sarah'] = 'c'
favorite_languajes['edward'] = 'ruby'
favorite_languajes['phil'] = 'python'


for name, languages in favorite_languajes.items():
    print(name.title()+ "'s favorite language is "+ languages.title()+ ".")
