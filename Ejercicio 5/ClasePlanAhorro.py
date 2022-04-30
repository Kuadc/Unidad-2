
class PlanAhorro():
    ''' Todos los planes de ahorro
        tienen las mismas cuotas'''
    Cantidad_cuotas = 60
    Cantidad_cuotas_pagas = 30

    def __init__(self,codigo=0,modelo=0,version=0,valor=0.0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    @classmethod
    def GetCant_Cuotas(cls):
        return cls.Cantidad_cuotas

    @classmethod
    def GetCant_Cuotaspagas(cls):
        return cls.Cantidad_cuotas_pagas

    def Getcodigo(self):
        return self.__codigo

    def Getmodelo(self):
        return self.__modelo

    def Getversion(self):
        return self.__version

    def Getvalor(self):
        return self.__valor

    def Getvalor2(self,unvalor):
        self.__valor = unvalor

    def __str__(self):
        return 'Codigo: {} \n Modelo: {} \n Version: {} \n Valor: {:.2f}'.format(self.__codigo,self.__modelo,self.__version,self.__valor)


