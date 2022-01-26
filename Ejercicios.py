
# creo la clase
class Perro():
    #siempre en un objeto crear el constructor.
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
    
    def ladrar(self):
        if self.peso > 3:
            print("Guau, Guau")
        else:
            print("ay, ay")
    def __str__(self):
        return "Guau, soy {} y peso {} kg".format( self.nombre, self.peso)