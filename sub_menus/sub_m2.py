import libreria

def partido1():
    partido=libreria.pedir_partido("ingrese partido:" )
    presidente=libreria.pedir_nombre("ingrese 1er candidato:")

    contenido=partido + " - " + presidente + "\n"
    libreria.guardar_datos("partido.txt", contenido, "a")
    print("datos guardados")

def partido2():
    partido=libreria.pedir_partido("ingrese partido:")
    presidente=libreria.pedir_nombre("ingrese 2do candidato")

    contenido=partido + " - " + presidente + "\n"
    libreria.guardar_datos("partido.txt", contenido, "a")
    print("datos guardados")
#Menus de Comando
opc=0
max=3


while( opc != max):
    #1. impresion del menu
    print("#############MENU#############")
    print("# 1. Primer partido politico #")
    print("# 2. Segundo partido politico#")
    print("# 3. salir                   #")
    print("##############################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:", 1, 3)

    if ( opc==1):
        partido1()
    if ( opc==2):
        partido2()

#fin_menu

print("fin del menu")
