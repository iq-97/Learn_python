# se utiliza la funcion open donde se pide un argumento donde el cual es el nombre del archivo a abrir
# esto se almacena en un objeto llamado file_object
file = 'one_million_pi_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines()

# working with a file's contents
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

#ejemplo
birthday = input("coloca tu fecha de cumpleanos asi mmddyy: ")

if birthday in pi_string:
    print("tu fecha de cumpleanos conside con una parte de los digitos de pi!")
else:
    print("tu fecha no coincide en el primer millon de digitos de pi!")