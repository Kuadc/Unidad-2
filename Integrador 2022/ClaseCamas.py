

class Cama():
    __idCama = 0
    __habitación = 0
    __estado = bool
    __apellidoNombre = None
    __diagnostico = ""
    __fechaInternacion =""
    __fechaAlta =None

    def __init__(self,id,ha,es,ap,diag,fint,falt=None):
        self.__idCama = id
        self.__habitación = ha
        self.__estado = es
        self.__apellidoNombre  = ap
        self.__diagnostico = diag
        self.__fechaInternacion = fint
        self.__fechaAlta = falt

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.__idCama,self.__habitación,self.__estado,self.__apellidoNombre,self.__diagnostico,self.__fechaInternacion,self.__fechaAlta)

    def Getnombre(self):
        return self.__apellidoNombre

    def Getdiag(self):
        return self.__diagnostico

    def DardeAlta(self):
        self.__fechaAlta = "2/5/2022"

    def Mostrarpaciente(self):
        print("Paciente: {}     Cama: {}        Habitacion: {}".format(self.__apellidoNombre,self.__idCama,self.__habitación))
        print("Diagnostico: {}          Fecha de Internacion: {}".format(self.__diagnostico, self.__fechaInternacion))
        print("Fecha de Alta: {}".format(self.__fechaAlta))
