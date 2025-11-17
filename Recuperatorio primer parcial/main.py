import os

from  funciones import *

from inputs import *

array_nombres = crear_array(6, 0)
matriz_clasificaciones = crear_matriz (6,3, 0)
bandera_clasificaciones = False
bandera_participantes =False
array_para_ordenar = [47, 12, 89, 5, 73, 34, 21, 98, 66, 40]

#Hardcodeo

# bandera_clasificaciones = True
# bandera_participantes =True
# array_nombres = ["pedro Sachez","ana frank","juan roman","leo messi","mayra mendoza", "arami garay "]
# matriz_clasificaciones = [
#     [10,7,9],
#     [2,3,2],
#     [6,9,2],
#     [3,4,5],
#     [5,8,7],
#     [2,4,1],
# ]

while True:
    print("1.Cargar nombre de los participantes ")
    print("2.Cargar clasificacion de los jueces  ")
    print("3.Mostrar calificaciones ")
    print("4.Mostrar participantes con promedio mayor a 4 ")
    print("5.Mostrar participantes con promedio mayor a 8")
    print("6.Mostrar jurado más estricto")
    print("7.Mostrar ganador ")
    print("8.Buscar participante por apellido")
    print("9.Ordenamiento ")
    print("10.Salir ")

    opcion = input("Ingrese su opcion: ")
    print("")
    if bandera_participantes == True:
        print ("Nombres ya cargados")
    if bandera_clasificaciones == True:
        print ("Clasificaciones cargadas")

    match opcion:
        case "1":
            if cargar_nombres(array_nombres) == True:
                print("Carga realizada con exito!")
                bandera_participantes = True
            else:
                print("Error al realizar la carga!")
        case "2":
            if cargar_clasificaciones(matriz_clasificaciones,array_nombres) == True:
                print("Carga realizada con exito")
                bandera_clasificaciones = True
            else:
                print("Error al realizar la carga!")
        case "3":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error datos no cargados")
            else:
                mostrar_clasificaciones(matriz_clasificaciones,array_nombres)
        case "4":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else :
                mostrar_participante_mayor_promedio(matriz_clasificaciones, array_nombres,4)
        case "5":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else :
                mostrar_participante_mayor_promedio(matriz_clasificaciones, array_nombres,8)
        case "6":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else:
                Mostrar_jurado_estrico(matriz_clasificaciones)
        case "7":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else:
                mostrar_ganador(matriz_clasificaciones,array_nombres)
        case "8":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else:
                encontrar_participante_por_apellido(array_nombres,matriz_clasificaciones)
        case "9":
            if bandera_clasificaciones == False and bandera_participantes ==False :
                print("Error")
            else:
                print(f"Arreglo antes: {array_para_ordenar} ")
                print("------------------------------------")
                arreglo_acendente = bubble_sort (array_para_ordenar,False)
                
                print(f"Arreglo despues (acendente): {arreglo_acendente} ")
                print("")
                arreglo_decendente = bubble_sort(array_para_ordenar, True)
                print(f"Arreglo despues (decendente): {arreglo_decendente} ")
        case "10":
            print("Saliendo...")
            break
    input("Toque cualquier boton para continuar...")
    os.system("clear")
