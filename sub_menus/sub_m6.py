import libreria

def Menu():
    menu=libreria.pedir_menu("ingrese su pedido:")

    contenido=menu + "\n"
    libreria.guardar_datos("comidas.txt", contenido, "a")
    print("datos guardados")

def PlatoCarta():
    plato_carta=libreria.pedir_nombre("ingrese su pedido:")

    contenido=plato_carta + "\n"
    libreria.guardar_datos("comidas.txt", contenido, "a")
    print("datos guardados")


def Ceviche():
    ceviche=libreria.pedir_nombre("ingrese ceviche de:")
    contenido=ceviche + "\n"
    libreria.guardar_datos("comidas.txt", contenido, "a")
    print("datos guardados")
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
