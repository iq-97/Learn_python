import json

# load the username, if it has been stored previously


def get_stored_user():
    """Get stored username if available"""
    filename = 'nombre_usuario.json'

    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_user():
    usuario = input("ingresa tu nombre: ")
    file_name = 'nombre_usuario.json'
    with open(file_name, 'w') as f_obj:
        json.dump(usuario,f_obj)
    return usuario

def greet_user():
    usuario = get_stored_user()

    if usuario:
        print("hola bienvenido de nuevo:" + usuario)
    else:
        usuario = get_new_user()
        print("te recordare cuando ingreses de nuevo: "+usuario)

greet_user()