prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
#se utilizan banderas en lugar de un operador condicional en el ciclo while
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        #si la condicion del if se cumple se coloca la bandera en un estado false y se termina el programa
        active = False
    else:
        print(message)