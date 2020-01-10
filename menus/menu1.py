import libreria

def juego_Accion():
    input("ingrese juego:")
    print("juego de accion elegida")

def juego_Estrategia():
    input("ingrese juego:")
    print("juego de estrategia elegida")

def juego_Carrera():
    input("ingrese juego:")
    print("juego de carreras elegida")

opc=0
max=4

while( opc != max):
    #1. impresion dl menu
    print("#############MENU##########")
    print("# 1. Juego de accion      #")
    print("# 2. Juego de estrategia  #")
    print("# 3. juego carrera        #")
    print("# 4. Salir                #")
    print("###########################")


    #2. Eleccion del opcion del menu
    opc=libreria.pedir_numero("Ingrese opcion:", 1, 4)

    #3. Mapeo de las opciones
    if ( opc == 1 ):
        juego_Accion()
    if ( opc == 2 ):
        juego_Estrategia()
    if ( opc == 3 ):
        juego_Carrera()

#fin_menu
print("fin de los juegos")
