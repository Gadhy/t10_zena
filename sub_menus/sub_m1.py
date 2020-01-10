import libreria

# Implementacion de sub menu
def juego_Accion_Spiderman():
    print("Opcion Spiderman elegida")

def juego_Accion_RedBall():
    print("opcion Red Ball elegida")

def juego_Accion():
    opc=0
    max=3
    while (opc != max):
        print("#########Juego de Accion#########")
        print("# 1. Spiderman                  #")
        print("# 2. Red Ball                   #")
        print("# 3. salir                      #")
        print("#################################")
        opc=libreria.pedir_numero("ingrese opcion:", 1, 3)
        if ( opc == 1):
            juego_Accion_Spiderman()
        if ( opc == 2):
            juego_Accion_RedBall()

# Implementacion de sub menu 2
def juego_Estrategia_AliensEmpires():
    print("Opcion A. Empires elegida")

def juego_Estrategia_DragonBound():
    print("opcion D. Bound elegida")

def juego_Estrategia():
    opc=0
    max=3
    while (opc != max):
        print("#######Juego de Estrategia#######")
        print("# 1. Aliens Empires             #")
        print("# 2. Dragon Bound               #")
        print("# 3. salir                      #")
        print("#################################")
        opc=libreria.pedir_numero("ingrese opcion:", 1, 3)
        if ( opc == 1):
            juego_Estrategia_AliensEmpires()
        if ( opc == 2):
            juego_Estrategia_DragonBound()

# Implementacion de sub menu 2


def juego_Carrera_Blur():
    print("Juego: Blur elegida")
def juego_Carrera_Motocrosfice():
    print("Juego: Motocrosfice elegida")

def juego_Carrera():
    opc=0
    max=3
    while (opc != max):
        print("#######Juego de Carrera#######")
        print("# 1. Blur                    #")
        print("# 2. Motocrosfice            #")
        print("# 3. salir                   #")
        print("##############################")
        opc=libreria.pedir_numero("ingrese opcion:", 1, 3)
        if ( opc == 1):
            juego_Carrera_Blur()
        if ( opc == 2):
            juego_Carrera_Motocrosfice()

opc=0
max=4

while( opc != max):
    #1. impresion del menu
    print("#############MENU##########")
    print("# 1. Juego de accion      #")
    print("# 2. Juego de estrategia  #")
    print("# 3. Juego de carrera     #")
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
