class car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = self.model+" "+self.make+" "+self.year+"."
        return long_name.title()


    def read_odometer(self):
        """devuelve la lectura de kilometros recorridos"""
        print("el total de kilometros recorridos es de: "+str(self.odometer))

    #creando metodo para modificar valor de read_odometer
    def update_odometer_read(self, recorrido):
        """modifica la lectura de kilometros recorridos"""
        if recorrido >= self.odometer:
            self.odometer = recorrido
        else:
            print("no puedes retroceder el conteo de kilometros recorridos")

    #creando metodo para incrementar kilometraje
    def increment_odometer_read(self, miles):
        """incrementa la lectura de kilometraje"""
        self.odometer += miles
#my_new_car = car('ford','focus','1968')
#cambiando el valor por defecto de odometer directamente despues de la instancia
#my_new_car.odometer = 23
#cambiando el valor por defecto de odometer utilizando un metodo
#my_new_car.update_odometer_read(150)
#my_new_car.read_odometer()
#my_new_car.increment_odometer_read(250)
#my_new_car.read_odometer()
#print(my_new_car.descriptive_name())
