import libreria
def Whatssap():
    print("Bienvenido a whatasap")


def Facebook():
    print("Bienvenido a Facebook")

def Messenger():
    print("opcion 3 elegida")

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
