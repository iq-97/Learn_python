filename = 'output.txt'
mensaje = input("Escribe el mensaje que saldra en el txt: ")
# modos que existen para abrir un archivo: w es modo de escritura, r modo lectura, 'a' modo de adjuntar,
# r+ que permite el modo de lectura y escritura
with open(filename, 'a') as file_object:
    file_object.write(mensaje)

print("mensaje escrito correctamente")