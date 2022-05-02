'''

Clase:

    ViajeroFrecuente:
    Atributos(int,string,string,string,int)

Funciones:

    Constructor(int,string,string,string,int)
    __str__(imprime el objeto)
'''

class ViajeroFrecuente:
    __num_viajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0

    def __init__(self, n=0,d="",nom="",ap="",millas=0):
        self.__num_viajero = n
        self.__dni = d
        self.__nombre = nom
        self.__apellido = ap
        self.__millas_acum = millas

    def GetMillas(self):
        return self.__millas_acum

    def __gt__(self, objeto2):
        if self.__millas_acum > objeto2.GetMillas():
            return True
        else:
            return False

    def __eq__(self, other):
        return self.__millas_acum == other

    def __add__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+other)

    #__radd__ = __add__  (tambien puede realizarse de esta manera)

    def __sub__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-other)

    def __rsub__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-other)

    def __str__(self):
        return "  %d %s %s %s %s" % (self.__num_viajero,self.__dni,self.__apellido,self.__nombre,self.__millas_acum)

    def __radd__(self, other):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+other)

    def Getviajero(self):
       return self.__num_viajero



