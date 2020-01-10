import libreria
def Nota1_ciclo():
    n1=libreria.pedir_numero("ingrese n1:", 1, 20)
    n2=libreria.pedir_numero("ingrese n2:", 1, 20)
    resultado=libreria.pedir_resultado((n1+n2)/2)

    contenido=resultado + "\n"
    libreria.guardar_datos("notas.txt", contenido, "a")
    print("Datos guardados")



def Nota2_ciclo():
    n1=libreria.pedir_numero("ingrese N1=", 1, 20)
    n2=libreria.pedir_numero("ingrese N2=", 1, 20)
    resultado=libreria.pedir_resultado((n1+n2)/2)

    contenido=resultado + "\n"
    libreria.guardar_datos("notas.txt", contenido, "a")
    print("Datos guardados")

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

