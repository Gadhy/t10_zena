import libreria
def Nota1_ciclo():
    n1=libreria.pedir_nota("ingrese n1:")
    n2=libreria.pedir_nota("ingrese n2:")
    print("el promedio del 1er ciclo es:", (n1 + n2)/2)

    contenido=n1 + "-" + n2 + "\n"
    libreria.guardar_datos("notas.txt", contenido, "a")
    print("Datos guardados")



def Nota2_ciclo():
    n1=libreria.pedir_numero("ingrese N1=", 0, 100)
    n2=libreria.pedir_numero("ingrese N2=", 0, 100)
    print("el promedio del 2do ciclo es:", (n1 + n2)/2)
#Menus de Comando
opc=0
max=3

while(opc != max):
    #1. impresion del menu
    print("#############MENU##########")
    print("# 1. Nota 1er ciclo       #")
    print("# 2. Nota 2do ciclo       #")
    print("# 3. Salir                #")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion:", 1, 3)


    if ( opc == 1):
        Nota1_ciclo()

    if (opc ==2):
        Nota2_ciclo()

