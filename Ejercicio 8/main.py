from ClaseConjunto import Conjunto
from ClaseMenu import Menu

if __name__ == '__main__':
    lista1= [1,2,3,4]
    lista2= [3,6,9]
    A = Conjunto(lista1)
    B = Conjunto(lista2)
    print(A)
    print(B)
    unmenu = Menu()
    while True:
        print('\n-------Menu--------')
        print("1) - Unión de dos conjuntos.")
        print("2) - La diferencia de dos conjuntos.")
        print("3) - Verificar si dos conjuntos son iguales")
        print("4) - Finalizar")
        opcion= input("\nIngrese la opcion Deseada: ")
        unmenu.opcion(opcion,A,B)

