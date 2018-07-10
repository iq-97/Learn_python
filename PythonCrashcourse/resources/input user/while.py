prompt = "dime algo, y lo repetire: \n ingresa 'quit' para finalizar el programa: "
mensaje = ""

while mensaje != 'quit':
    mensaje = input(prompt)
    if mensaje != 'quit':
        print(mensaje)
