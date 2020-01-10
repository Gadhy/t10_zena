import libreria
def Whatssap():
    aplicacion=libreria.pedir_aplicacion("ingrese aplicacion:" )
    numero_tel=libreria.pedir_numero_tel("ingrse el nro de tel:")

    contenido=aplicacion + " - " + numero_tel + "\n"
    libreria.guardar_datos("aplicacion.txt", contenido, "a")
    print("datos guardados")

def Facebook():
    aplicacion=libreria.pedir_aplicacion("ingrese aplicacion:")

    contenido=aplicacion +  "\n"
    libreria.guardar_datos("aplicacion.txt", contenido, "a")
    print("datos guardados")

def Messenger():
    aplicacion=libreria.pedir_aplicacion("ingrese aplicacion:")
    contenido=aplicacion +  "\n"
    libreria.guardar_datos("aplicacion.txt", contenido, "a")
    print("datos guardados")

#Menus de Comando
opc=0
max=4

while( opc != max):
    #1. impresion dl menu
    print("#############MENU##########")
    print("# 1. Whatssap             #")
    print("# 2. Facebook             #")
    print("# 3. Messenger            #")
    print("# 4. Salir                #")
    print("###########################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if ( opc==1):
        Whatssap()

    if ( opc==2):
        Facebook()

    if ( opc==3):
        Messenger()

#fin_menu
print("fin del menu")
