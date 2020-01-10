import libreria

def Potencia():
    trabajo=libreria.pedir_numero("ingrese trabajo:", 1, 20)
    tiempo= libreria.pedir_numero("ingrese tiempo:", 1, 20)
    resultado=libreria.pedir_resultado(trabajo/tiempo)

    contenido= resultado + "\n"
    libreria.guardar_datos("Calculos.txt", contenido, "a")
    print("datos guardados")

def Calor():
    masa=libreria.pedir_numero("ingrese masa:", 1, 20)
    ce= libreria.pedir_numero("ingrese calor:", 1, 20)
    temp=libreria.pedir_numero("ingrese temperatura", 1, 20)
    resultado=libreria.pedir_resultado(masa*ce*temp)

    contenido= resultado "\n"
    libreria.guardar_datos("Calculos.txt", contenido, "a")
    print("datos guardados")

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
        Potencia()

    if ( opc.upper() == "CALOR"):
        Calor()
