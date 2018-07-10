mascotas = ['gato','perro','loro','gallina']
prompt = "ingrese el nombre de la mascota a eliminar: "
print("este es el listado de animales a eliminar: ")
for mascota in mascotas:
    print(mascota)

pet = input(prompt)

#removing specific value
while pet in mascotas:
    for mascota in mascotas:
        if pet == mascota:
            mascotas.remove(pet)
        else:
            print("no existe mascota")


print(mascotas)