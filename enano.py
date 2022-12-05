from personaje import Personaje

class Enano(Personaje):

    def __init__(self, nombre, raza, arma, vida, daño, bonificacion,clan):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion)
        self.__clan = clan

    def __str__(self):
        return super().__str__()+" - Clan: {}".format(self.__clan)

    def GetClan(self):
        return self.__clan

    def SetClan(self,clan):
        self.__clan = clan

    def Historia(self):
        pass

    def Victoria(self):
        pass

    def Derrota(self):
        pass

    def AumentaVida(self):
        aumento =int(input("Ingrese el aumento de vida (Entre 50 y 100): "))
        while aumento < 50 or aumento > 100:
            aumento = int(input("Ingrese un aumento de vida válido (Entre 50 y 100): ")) 
        vidabase = self.GetVida()
        aumento2 = vidabase + int(aumento)
        self.SetVida(aumento2)
        print("Se ha aumentado la vida {} pts\nVida actual: {}".format(aumento,aumento2))