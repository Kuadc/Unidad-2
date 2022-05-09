
class Conjunto():
    __conj = []

    def __init__(self,lista):
        self.__conj = lista

    def __eq__(self, other):
        a= len(self.__conj)
        b= len(other.__conj)
        i=0
        bandera = None
        if a == b:
            self.__conj.sort()
            other.__conj.sort()
            while i < a:
                if self.__conj[i] == other.__conj[i]:
                    i+=1
            if i==a:
                return True
        else:
            return False

    def __str__(self):
        return "Lista: %s" % self.__conj

    def __add__(self, other):
        self.__conj.sort()
        other.__conj.sort()
        a = len(self.__conj)
        b = len(other.__conj)
        i = 0
        j = 0
        lista = []
        while i<a and j<b:
            if self.__conj[i] < other.__conj[j]:
                lista.append(self.__conj[i])
                i+=1
            elif self.__conj[i] == other.__conj[j]:
                lista.append(other.__conj[j])
                i+= 1
                j+=1
            else:
                lista.append(self.__conj[i])
                i+=1
                j+=1
        if i<a:
            while i<a:
                lista.append(self.__conj[i])
                i+=1
        if j<b:
            while j<b:
                lista.append(other.__conj[j])
                j+=1
        return Conjunto(lista)


    def __sub__(self, other):
        a = len(self.__conj)
        b = len(other.__conj)
        i=0
        lista = []
        j=0
        while i<a:
            x = self.__conj[i] not in other.__conj
            if x:
                lista.append(self.__conj[i])
                i+=1
            else:
                i+=1

        return Conjunto(lista)






