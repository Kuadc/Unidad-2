import re


class ClaseEmail:
    def __init__(self, id="", domi="", com="", contra=1234):
        self.__idcuenta = id
        self.__dominio = domi
        self.__tipodominio = com
        self.__contraseña = contra

    def retornamail(self):
        print(" correo = {}@{}.{}".format(self.__idcuenta, self.__dominio, self.__tipodominio))

    def getdominio(self):
        print("dominio =", self.__dominio)

    def crearcuenta(self, p):
        p = re.split('[@.]',p)
        self.__idcuenta = p[0]
        self.__dominio = p[1]
        self.__tipodominio = p[2]
        print("Esta es la nueva dirección guardada : {}@{}.{}".format(self.__idcuenta, self.__dominio,self.__tipodominio))


    def mostrarDatos(self):
        print("Direccion" ,(self.__idcuenta, self.__dominio,self.__tipodominio))

    def CompararDatos(self,unmail):
        i=0
        if self.__idcuenta == unmail:
            i+=1
        return(i)

    def crearmail(self):
        nombre = input("Ingrese su nombre: ")
        self.__idcuenta = input("Ingrese el identificar de la cuenta: ")
        self.__dominio = input("Ingrese dominio: ")
        self.__tipodominio = input("Ingrese el tipo de dominio: ")
        self.__contraseña = input("Ingrese su contraseña: ")
        print("Estimado ", nombre,
              "te enviaremos tus mensajes a la direccion : {}@{}.{}".format(self.__idcuenta, self.__dominio,
                                                                            self.__tipodominio))

    def CrearDesdeLista(self):
        for i in range(10):
            m = self.__ListaEmail[0][0]
            email1 = ClaseEmail()
            email.crearcuanta(m)

    def modificarcontraseña(self):
        contra = input("Igrese la contraseña su contraseña actual: ")
        if contra == self.__contraseña:
            self.__contraseña = input("Ingrese la nueva contraseña: ")
        else:
            print("Contraseña incorrecta")




