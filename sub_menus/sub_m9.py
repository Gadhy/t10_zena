import libreria
def Dni():
    input("ingrese numero:")
    print("dni eledigo")


def f_Nacimiento():
    dia=libreria.pedir_numero("ingrese dia:", 1, 30)
    ano=libreria.pedir_numero("ingrese ano:", 1, 9999)
    mes=libreria.pedir_numero("ingrese mes", 1, 12)
    fecha=libreria.pedir_fecha("la fecha es:")

    contenido= dia + "-" + mes + "-" + ano+ "\n"
    libreria.guardar_datos("Calculos.txt", contenido, "a")
    print("datos guardados")



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


