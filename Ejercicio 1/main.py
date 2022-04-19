from Email import ClaseEmail
from ManejadoEmail import arregloNumpy


# Programa principal
if __name__ == '__main__':
    x = ClaseEmail()
    x.crearmail()
    x.modificarcontraseña()
    z = ClaseEmail()
    unmail = input("Ingrese su email: ")
    z.crearcuenta(unmail)
    arregloEmail = arregloNumpy(10,10)
    arregloEmail.ManejadorArchivo()
    arregloEmail.mostraremails()
    print("\n\n------Vamos a Buscar un Identificador de cuenta-------")
    arregloEmail.buscarEmail()
