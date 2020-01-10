import libreria
def Dni():
    input("ingrese numero:")
    print("dni eledigo")


def f_Nacimiento():
    input("ingrese f. Nacimiento:")
    print("Partida nacimiento elegida")



#Menus de Comando
opc=0
max=3

while( opc != max):
    #1. impresion dl menu
    print("##################MENU################")
    print("# 1. Agregar DNI                     #")
    print("# 2. Agregar Fecha de nacimiento     #")
    print("# 3. Salir                           #")
    print("######################################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:", 1, 3)

    if ( opc==1):
        Dni()

    if ( opc==2):
        f_Nacimiento()

    if ( opc==3):
        a_Acuaticos()

#fin_menu
print("fin del menu")


