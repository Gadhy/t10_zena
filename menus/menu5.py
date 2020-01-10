import libreria
def a_Terrestres():
    input("ingrese animal terrestre:")
    print("Animal terrestre elegida")


def a_Aereos():
    input("ingrese animal aerea:")
    print("Animal aereo elegida")

def a_Acuaticos():
    input("ingrese animal acuatico:")
    print("Aniaml acuatico elegidan")

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


