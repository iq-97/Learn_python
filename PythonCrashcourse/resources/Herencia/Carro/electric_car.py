import car
class carro_electrico(car.car):
    """a simple attempt to represent a electric car"""

    def __init__(self, make,model,year):
        super().__init__(make, model, year)
        self.bateria = 70

    def ver_carga(self):
        print("la duracion de bateria es de : "+str(self.bateria))

tesla =carro_electrico('tesla','z 1','2018')
print(tesla.descriptive_name())
tesla.ver_carga()
tesla.update_odometer_read(80)
tesla.read_odometer()
