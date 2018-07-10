import car

class CarroElectrico(car.car):
    """a simple attempt to represent a electric car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.bateria = Battery()

   # def ver_carga(self):
         # print("la duracion de bateria es de : "+str(self.bateria))
# instances as attributes
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size=85):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a "+str(self.battery_size)+"-KWh battery.")

    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "this car can go approximately "+ str(range)
        message += " miles on a full charge."
        print(message)


tesla =CarroElectrico('tesla', 'z 1', '2018')
print(tesla.descriptive_name())
tesla.bateria.describe_battery()
tesla.bateria.get_range()
tesla.update_odometer_read(80)
tesla.read_odometer()
