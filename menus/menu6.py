import libreria

def Menu():
    input("Elegir Menu:")
    print("se elegio el menu")
def PlatoCarta():
    input("Eligir plato a la carta:")
    print("se elegio el plato a la carta")
def Ceviche():
    print("Elegir ceviche de:")
    print("se elegio el ceviche")
# Menu General
opc=0
max=4
while( opc != max):
    #1. impresion dl menu
    print("#############MENU##########")
    print("# 1. Menu                 #")
    print("# 2. Plato a la carta     #")
    print("# 3. Ceviche              #")
    print("# 4. Salir                #")
    print("###########################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 4)

    #3. Mapeo de las opciones
    if ( opc == 1 ):
        Menu()
    if ( opc == 2 ):
        PlatoCarta()
    if ( opc == 3 ):
        Ceviche()





#fin_menu
print("Fin del menu")
