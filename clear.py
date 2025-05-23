

class Pajaro:
    alas= True  #Atributo de la clase para todos

    def __init__(self, color,especie):  #Constuctor con elementos para cada instancia
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"el pajaro volo {metros}")    

    def pintar_negro(self):
        self.color = "negro"

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira")   


Pajaro.poner_huevos(2)
Pajaro.mirar()
