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
    def __str__(self):

        return "  %d %s %s %s %s" % (self.__num_viajero,self.__dni,self.__apellido,self.__nombre,self.__millas_acum)

    def Getviajero(self):
       return self.__num_viajero

    def __getitem__(self, item):
        return self.__millas_acum


    #def acumularMillas(self, num):
        #recibe cantidad de millas recorridas, las suma y retorna en valor actualizado


    #def canjearMillas(self, num):
        # recibe cantidad de millas a canjear
        # debe verificarse que la cantidad a canjear sea menor o igual a la cantidad de millas acumuladas,
        # caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad de millas acumuladas.
