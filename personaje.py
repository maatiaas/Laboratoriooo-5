class Personaje():

    def __init__(self,nombre,raza,arma,vida,daño,bonificacion):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__daño = daño
        self.__bonificacion = bonificacion

    def __str__(self):
        return "Nombre: {} - Raza: {} - Arma: {} - Vida: {} - Daño: {} - Bonificación: {}".format(self.__nombre,self.__raza,self.__arma,self.__vida,self.__daño,self.__bonificacion)
    
    def GetNombre(self):
        return self.__nombre

    def SetNombre(self,nombre):
        self.__nombre = nombre

    def GetRaza(self):
        return self.__raza

    def Raza(self,raza):
        self.__raza = raza

    def GetArma(self):
        return self.__arma

    def SetArma(self,arma):
        self.__arma = arma

    def GetVida(self):
        return self.__vida

    def SetVida(self,vida):
        self.__vida = vida

    def GetDaño(self):
        return self.__daño

    def SetDaño(self,daño):
        self.__daño = daño

    def GetBonificacion(self):
        return self.__bonificacion

    def Bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def Historia(self):
        pass

    def Victoria(self):
        pass

    def Derrota(self):
        pass

    def MensajeInicial(self):
        pass