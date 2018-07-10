def get_fullname(first_name, last_name, middle_name = ' '):#se pueden agregar parametros opcionales
    """funcion para concatenar nombre"""
    full_name = first_name+' '+middle_name+' '+last_name
    return full_name #returnara el nombre completo a donde este localizada la llamada de la funcion

#la variable cantante obtendra el valor que retornara la funcion
cantante = get_fullname('jimi','hendrix','lee')
#se imprime el valor que se retorno
print(cantante);


def build_person(first_name, last_name, edad=''):#agregando informacion adicional
    person = {'first': first_name, 'second': last_name}
    if edad:
        person['edad']=edad
    return person


persona = build_person('hector','felipe', edad=18)

print(persona)
