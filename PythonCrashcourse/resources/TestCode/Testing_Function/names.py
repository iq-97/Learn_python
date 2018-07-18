from name_function import get_formatted_name

print("ingresa 'q' para salir en cualquier momento. ")

while True:
    first = input("Ingresa tu primer nombre: ")
    if first == 'q':
        break
    last = input("Ingresa tu apellido: ")
    if last == 'q':
        break

    formated_name = get_formatted_name(first,last)
    print("tu nombre formateado es: "+formated_name)

