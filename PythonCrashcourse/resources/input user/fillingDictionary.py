#empty dictionary
responses = {}

polling_active = True

while polling_active:

    name = input("cua el es tu nombre: ")
    response = input("Que montania te gustaria subir algun dia: ")

    #almacenar la respuesta de la persona al diccionario
    responses[name] = response

    pregunta = input("quieres agregar a alguien mas? y/n: ")

    if pregunta == 'n':
        polling_active = False
    elif pregunta == 'y':
        polling_active = True
        
print("imprimiendo resultados: ")

for name, response in responses.items():
    print(name + "la montania que te gustaria visitar es: "+ response)


