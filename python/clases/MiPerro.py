class MiPerro:
    """ Clase con init q se ejecuta luego de instanciarse automaticamente """
    
    raza = ""

    def __init__(self,nuevaRaza): #self siempre se pone por default
        self.raza = nuevaRaza
        print("Creaste un perro de raza: ", self.raza)
        
    def ladrar(self,ladrido):
        print(ladrido)
    
    def jugar(self,jugar):
        print(jugar)

    def getRaza(self):
        print("Soy raza: ", self.raza)

parker = MiPerro("Poodle")
parker.ladrar("Guau")
parker.getRaza()