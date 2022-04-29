
class objeto():
    __temperatura = 0
    __humedad = 0
    __presion = 0

    def __init__(self,temp=0,humedad=0,presion=0):
        self.__temperatura = temp
        self.__humedad = humedad
        self.__presion = presion
    def Variablepresion(self):
        return self.__presion
    def getvariable(self):
        print( str(self.__temperatura)+ ','+ str(self.__presion))

    def GetItem_presion(self):
        return self.__presion

    def GetItem_temp(self):
        return self.__temperatura

    def GetItem_hum(self):
        return self.__humedad
    def __str__(self):
        return str(self.__temperatura) +','+ str(self.__humedad)+ ','+str(self.__presion)
