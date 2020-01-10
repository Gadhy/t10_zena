import libreria

def a_Terrestres():
    anim_trr=libreria.pedir_nombre("ingrese animal:")

    contenido=anim_trr + "\n"
    libreria.guardar_datos("animales.txt", contenido, "a")
    print("datos guardados")


def a_Aereos():
    anim_aer=libreria.pedir_nombre("ingrese animal:")

    contenido=anim_aer + "\n"
    libreria.guardar_datos("animales.txt", contenido, "a")
    print("datos guardados")

def a_Acuaticos():
    anim_acuat=libreria.pedir_nombre("ingrese animal:")

    contenido=anim_acuat + "\n"
    libreria.guardar_datos("animales.txt", contenido, "a")
    print("datos guardados")

#Menus de Comando
opc=0
max=4

while( opc != max):
    #1. impresion dl menu
    print("#############MENU##########")
    print("# 1. Animales terrestres  #")
    print("# 2. Animales aereos      #")
    print("# 3. Animales acuaticos   #")
    print("# 4. Salir                #")
    print("###########################")

    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:", 1, 4)

    if ( opc==1):
        a_Terrestres()

    if ( opc==2):
        a_Aereos()

    if ( opc==3):
        a_Acuaticos()

#fin_menu
print("fin del menu")


