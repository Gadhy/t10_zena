import libreria

def Trio1():
    libreria.pedir_nombre("ingrese su pedido:")
    print("Gracias por la eleccion")

def Trio2():
    libreria.pedir_nombre("ingrese su pedido:")
    print("Gracias por la eleccion")

#Menus de Comando
opc=0
max=3

while( opc != max):
    #1. impresion del menu
    print("#############MENU##########")
    print("# 1. Trio1                #")
    print("# 2. Trio2                #")
    print("# 3. Salir                #")
    print("###########################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:", 1, 3)

    if ( opc==1):
        Trio1()

    if ( opc==2):
        Trio2()

#fin_menu
print("fin del menu")
