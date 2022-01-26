class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        
        elif self.peso >=8:
            print("Guau, Guau")
        
        else:
            print("ay, ay")