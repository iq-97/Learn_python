class persona():
    def __init__(self, nombre, apellido, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = 18

    def datos_completos(self):
        print("tu nombre es: "+self.nombre+" tu apellido es: "+self.apellido+" tu sexo es: "+self.sexo)

    def correr(self):
        print("El humano llamdo "+self.nombre+" corre")

    def edad_maxima(self):
        print("edad maxima de: "+str(self.edad))
