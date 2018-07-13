# An attempt to show a ZeroDivisionError exception
#using a try except block

print("dame dos numeros, y estos se dividiran")
print("coloca q para salir")

while True:
    first_number = input("\ncoloca el primer numero: ")
    if first_number == 'q':
        break
    second_number = input("\ncoloca el segundo numero: ")
    if second_number == 'q':
        break
    # se coloca en el bloque try, unicamente operaciones que pueden ocasionar algun error
    # lo que dependa de try se coloca en el bloque else
    try:
        resultado = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("error no puedes dividir por 0")
    else:
        print(resultado)