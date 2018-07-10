#definiendo una funcion
def greet_user(name_user):#pasar informacion a una funcion
    """muestra un mensaje."""
    #desplegando mensaje
    print("hola mundo a: "+name_user)
#definiendo una funcion
def describe_pet(pet_name,animal_type='dog'):#parametros, ademas se le agrega un valor por defecto
    """Informacion sobre la mascota """
    print("i have a: "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name+".")

#si se utiliza un valor por defecto, pero el tipo no es el que se requiere, entonces
#se a la llamada de la funcion se coloca el tipo que es y omitira el valor por defecto que se tenga
#se llama a una funcion se envia informacion
greet_user('pedro')
#omitiendo el valor por de defecto
describe_pet(pet_name='suculento',animal_type='cat')#pasando argumentos por posicion
