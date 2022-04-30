
class Ventana():
    __titulo = ""
    __xSupIzq = 0
    __ySupIzq = 0
    __xInfDer = 500
    __yInfDer = 500

    def __init__(self,titulo="",xi=0,yi=0,xd=500,yd=500):
        if xi <xd and yi <yd:
            self.__titulo = titulo
            self.__xSupIzq = xi
            self.__ySupIzq = yi
            self.__xInfDer = xd
            self.__yInfDer = yd
        else:
            print("Parametro incorrectos")

    def mostrar(self):
        print("Titulo:",self.__titulo)
        print("Vertice X sup. Izq:{}, Vertice Y sup. Izq:{} , Vertice X Inf. Der: {}, Vertice Y Inf Dere:{}".format(self.__xSupIzq,self.__ySupIzq,self.__xInfDer,self.__yInfDer))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        if self.__ySupIzq == 0:
            alto=self.__ySupIzq + self.__yInfDer
        else:
            alto=self.__ySupIzq - self.__yInfDer
        return (alto)

    def ancho(self):
        if self.__xSupIzq == 0:
            ancho=self.__xSupIzq + self.__xInfDer
        else:
            ancho=self.__xSupIzq - self.__xInfDer
        return (ancho)

    def moverDerecha(self,num):
        if type(num)==int:
            self.__xInfDer +=num
            self.__xSupIzq +=num
        else:
            print("El valor pasado por parametro no es del tipo entero")

    def moverIzquierda(self,num):
        if type(num)==int:
            self.__xSupIzq -=num
            self.__xInfDer -=num
        else:
            print("El valor pasado por parametro no es del tipo entero")

    def bajar(self,num=0):
        if type(num)==int:
            self.__ySupIzq +=num
            self.__yInfDer +=num
        else:
            print("El valor pasado por parametro no es del tipo entero")

    def subir(self,num=0):
        if type(num)==int:
            self.__yInfDer -=num
            self.__ySupIzq -=num
        else:
            print("El valor pasado por parametro no es del tipo entero")
