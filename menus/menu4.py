import libreria
def opcionPotencia():
    input("ingrese potencia:")
    print("opcion: potencia elegida")



def opcionCalor():
    input("ingrese calor:")
    print("opcion: calor elegida")
#Menus de Comando
opc=0
fin="Salir"

while( opc != fin):
    #1. impresion del menu
    print("#############MENU###############")
    print("Potencia: calcular la potencia #")
    print("Calor: calcular el calor       #")
    print("Salir                          #")
    print("################################")

    opc=libreria.pedir_nombre("ingrese opcion:")

    if ( opc.upper() == "POTENCIA" ):
        opcionPotencia()

    if ( opc.upper() == "CALOR"):
        opcionCalor()
