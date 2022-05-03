
class Medicamento():
    __idCama = 0
    __idMedicamento = 0
    __nombreComercial = ""
    __monodroga = ""
    __presentacion= ""
    __cantidadAplicada = 0
    __precioTotal = 0.0

    def __init__(self,id,med,nomb,mono,pres,cant,precio):
        self.__idCama = id
        self.__nombreComercial = nomb
        self.__idMedicamento = med
        self.__monodroga = mono
        self.__presentacion = pres
        self.__cantidadAplicada = cant
        self.__precioTotal = precio

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.__idCama,self.__idMedicamento,self.__nombreComercial,self.__monodroga,self.__presentacion,self.__cantidadAplicada,self.__precioTotal)

    def idcama(self):
        return self.__idCama

    def GetNombre_comer(self):
        return self.__nombreComercial

    def GetMonodroga(self):
        return self.__monodroga

    def GetPresentacion(self):
        return self.__presentacion

    def GetCantidad(self):
        return self.__cantidadAplicada

    def GetPrecio(self):
        return self.__precioTotal

