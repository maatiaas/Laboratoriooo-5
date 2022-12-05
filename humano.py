from personaje import Personaje

class Humano(Personaje):

    def __init__(self, nombre, raza, arma, vida, daño, bonificacion,familia):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__familia = familia

    def __str__(self):
        return super().__str__()+" - Familia: {}".format(self.__familia)

    def GetFamilia(self):
        return self.__familia

    def Familia(self,familia):
        self.__familia = familia

    def Historia(self):
        pass

    def Victoria(self):
        pass

    def Derrota(self):
        pass
    
    def superBono(self):
        pass