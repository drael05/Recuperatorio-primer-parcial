import os

from  funciones import *

from inputs import *

array_nombres = crear_array(6, 0)
matriz_puntuaciones = crear_matriz (6,3, 0)
bandera_puntuaciones = False
bandera_participantes =False
array_para_ordenar = [47, 12, 89, 5, 73, 34, 21, 98, 66, 40]

while True:
    print("1.Cargar nombre de los participantes")
    print("2.Cargar puntuacion de los jueces ")
    print("3.Mostrar puntuaciones")
    print("4.Mostrar participantes con promedio mayor a 4 ")
    print("5.Mostrar participantes con promedio mayor a 8")
    print("6.Mostrar jurado más estricto")
    print("7.Mostrar ganador ")
    print("8.Buscar participante por apellido")
    print("9.Ordenamiento ")
    print("10.Salir ")
    
    if bandera_participantes == True:
        print ("-----NOMBRES YA CARGADOS-----")
    if bandera_puntuaciones == True:
        print ("-----PUNTUACIONES YA CARGADAS-----")
    opcion = input("Ingrese su opcion: ")
    print("")

    match opcion:
        case "1":
            if cargar_nombres(array_nombres) == True:
                print("Carga realizada con exito!")
                bandera_participantes = True
            else:
                print("Error al realizar la carga!")
        case "2":
            if cargar_puntuaciones(matriz_puntuaciones,array_nombres) == True:
                print("Carga realizada con exito")
                bandera_puntuaciones = True
            else:
                print("Error al realizar la carga!")
        case "3":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else:
                mostrar_puntuaciones(matriz_puntuaciones,array_nombres)
        case "4":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else :
                mostrar_participante_mayor_promedio(matriz_puntuaciones, array_nombres,4)
        case "5":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else :
                mostrar_participante_mayor_promedio(matriz_puntuaciones, array_nombres,8)
        case "6":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else:
                Mostrar_jurado_estrico(matriz_puntuaciones)
        case "7":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else:
                mostrar_ganador(matriz_puntuaciones,array_nombres)
        case "8":
            if bandera_puntuaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else:
                encontrar_participante_por_apellido(array_nombres,matriz_puntuaciones)
        case "9":
                print(f"----- Arreglo antes: {array_para_ordenar} -----")
                print("")
                arreglo_acendente = bubble_sort (array_para_ordenar)
                print(f"Arreglo despues (mayor a menor): {arreglo_acendente} ")
        case "10":
            print("Saliendo...")
            break
    input("Toque cualquier boton para continuar...")
    os.system("cls")
