class MiClaseEjemplo:
    """ Ejemplo de clase, objeto y metodos """
    
    entero = 4321

    def mensaje(self, msj):
        return msj

#Instancia la clase
x = MiClaseEjemplo()
y = MiClaseEjemplo()

#La uso
print(x.entero)
print(y.mensaje("Hola q hace"))
