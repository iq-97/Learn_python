import persona
class estudiante(persona.persona):
    def __init__(self,nombre, apellido, sexo):
        super().__init__(nombre, apellido, sexo)
        self.calificacion =70

    def establecer_religion(self):
        """Funcion spara colocar su religion"""
        print("tu nota es: "+str(self.calificacion))

estudiante1 = estudiante('hector','felipe','masculino')
estudiante1.datos_completos()
estudiante1.edad_maxima()
estudiante1.correr()
estudiante1.establecer_religion()
