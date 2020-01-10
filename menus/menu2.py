import libreria
def partido1():
    libreria.pedir_nombre("ingrese partido:")
    print("Partido elegido")
def partido2():
    libreria.pedir_nombre("ingrese partido")
    print("Partido elegido")
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
