from inputs import * 


def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    return array

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def calcular_promedio(acumulador:int | float,contador:int,mensaje_error:str = "error desconocido") -> float | int | str:
    if contador != 0:
        promedio = round((acumulador / contador),2)
        
        if promedio == int(promedio):
            promedio = int(promedio)
    else:
        promedio = mensaje_error
        
    return promedio

def sumar_fila(matriz:list,indice_fila:int) -> int | float:
    suma = 0
    
    if type(matriz) == list and type(indice_fila) == int:
        if len(matriz) > indice_fila and indice_fila >= 0:
            for col in range(len(matriz[indice_fila])):
                if (type(matriz[indice_fila][col]) == int or type(matriz[indice_fila][col]) == float):
                    suma += matriz[indice_fila][col]
    
    return suma


def calcular_promedio_nota_participante(matriz:list,indice:int)->int:
    suma_notas = sumar_fila(matriz, indice)
    cantidad_puntuaciones = len(matriz[indice])
    promedio = calcular_promedio(suma_notas, cantidad_puntuaciones)
    return promedio

def mostrar_resultado(array_nombres:list,matriz_puntuaciones:list,indice:int) -> bool:
    retorno = False
    
    if type(matriz_puntuaciones) == list and len(matriz_puntuaciones) > 0 and type(array_nombres) == list and len(array_nombres) > 0 and type(matriz_puntuaciones[indice]) == list:
        promedio_puntuaciones = calcular_promedio_nota_participante(matriz_puntuaciones,indice)
        mostrar_nombre_y_apellido(array_nombres[indice])
        print(f"Puntuacion jurado 1: {matriz_puntuaciones[indice][0]} /10 ")
        print(f"Puntuacion jurado 2: {matriz_puntuaciones[indice][1]} /10 ")
        print(f"Puntuacion jurado 3: {matriz_puntuaciones[indice][2]} /10 ")
        print(f"Promedio de  nota: {promedio_puntuaciones} /10")
        retorno = True
    return retorno

def mostrar_puntuaciones(matriz_puntuaciones:list,array_nombres:list) -> bool:
    retorno = False
    
    if type(matriz_puntuaciones) == list and len(matriz_puntuaciones) > 0 and type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            if type(matriz_puntuaciones[i]) == list:
                mostrar_resultado(array_nombres,matriz_puntuaciones,i)
                print("")
                retorno = True

    return retorno

def mostrar_nombre_y_apellido(cadena:str):
    nombre = encontrar_nombre(cadena)
    print(f"Nombre: {nombre}")
    apellido = encontrar_apellido(cadena)
    print(f"Apellido: {apellido}")


def encontrar_nombre(cadena:str)-> str:
    cadena_copia = ""
    if len(cadena) > 0:
        for i in range (len(cadena)):
            valor_a_comparar = ord(cadena[i])
            if valor_a_comparar == 32:
                break
            else:
                cadena_copia += cadena[i]
    return cadena_copia

def encontrar_apellido (cadena:str)-> str:
    cadena_copia = ""
    bandera_espacio = False
    if len(cadena) > 0:
        for i in range (len(cadena)):
            valor_a_comparar = ord(cadena[i])
            if valor_a_comparar == 32:
                bandera_espacio = True
            elif bandera_espacio == True:
                cadena_copia += cadena[i]
    return cadena_copia


def mostrar_participante_mayor_promedio(matriz_puntajes:list,array_nombres:list,porcentaje_maximo:int|float) -> bool:
    retorno = False
    
    if type(matriz_puntajes) == list and len(matriz_puntajes) > 0 and type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(matriz_puntajes)):
            porcentaje = calcular_promedio_nota_participante(matriz_puntajes,i)
            
            if porcentaje  > porcentaje_maximo:
                mostrar_resultado(array_nombres,matriz_puntajes,i)
                print("")
                retorno = True
                
    return retorno

def sumar_columna(matriz:list,indice_columna:int) -> int | float:
    suma = 0 
    if type(matriz) == list:
        for fil in range(len(matriz)):
            if indice_columna < len(matriz[fil]) and indice_columna >= 0 and type(matriz[fil]) == list:
                if type(matriz[fil][indice_columna]) == int or type(matriz[fil][indice_columna]) == float:
                    suma += matriz[fil][indice_columna]
    
    return suma

def encontrar_minimo_columna(matriz_puntuaciones:list)-> int | float:
    bandera = False
    
    for col in range(len(matriz_puntuaciones[0])):
        suma = sumar_columna(matriz_puntuaciones,col)
        
        if bandera == False:
            minimo = suma
            bandera = True
        else:
            if suma < minimo:
                minimo = suma
            
    return minimo

def Mostrar_jurado_estrico(matriz_puntuaciones:list)->bool :
    retorno = False
    if type(matriz_puntuaciones) == list:
        retorno = True
        valor_minimo = encontrar_minimo_columna(matriz_puntuaciones)
        print("Los jurados mas estricos son: ")
        for col in range (len(matriz_puntuaciones)):
            suma = sumar_columna(matriz_puntuaciones,col) 
            if valor_minimo == suma:
                print(f"Jurado {col + 1}")
            else:
                retorno = False
    else:
        retorno = False
    return retorno


def encontrar_promedio_maximo_fila(matriz:list) -> int | float:
    bandera = False
    
    for fil in range(len(matriz[0])):
        promedio = calcular_promedio_nota_participante(matriz,fil)
        
        if bandera == False:
            maximo = promedio
            bandera = True
        else:
            if promedio > maximo:
                maximo = promedio
            
    return maximo

def mostrar_ganador (matriz_puntuaciones:list, array_nombres:list)->bool:
    if type(matriz_puntuaciones) == list and len(matriz_puntuaciones) > 0 and type(array_nombres) == list and len(array_nombres) > 0:
        retorno = True
        valor_maximo = encontrar_promedio_maximo_fila(matriz_puntuaciones)
        lista_nombre_ganador = []
        lista_promedio_ganador = []
        for fil in range (len(matriz_puntuaciones)):
            promedio = calcular_promedio_nota_participante(matriz_puntuaciones,fil)
            if valor_maximo == promedio:
                lista_nombre_ganador = lista_nombre_ganador + [array_nombres[fil]]
                lista_promedio_ganador =  lista_promedio_ganador + [promedio]
        if len(lista_nombre_ganador) == 1:
            print(f"EL GANADOR ES: {lista_nombre_ganador[0]}")
            print(f"SU PROMEDIO FUE: {lista_promedio_ganador[0]}/10")
        else: 
            print (F"EMPATARON {len(lista_nombre_ganador)} PARTICIPANTES:")
            for i in range (len(lista_nombre_ganador)):
                print(f"{lista_nombre_ganador[i]}")
            print(f"CON UN PROMEDIO FINAL DE : {lista_promedio_ganador[0]}/10")
    else:
        retorno = False
        return retorno

def encontrar_participante_por_apellido(array_nombres:list, matriz_puntuaciones:list)->bool:
    retorno = True
    
    if type(array_nombres) == list and len(array_nombres) > 0 and type(matriz_puntuaciones) == list and len(matriz_puntuaciones) > 0 :
        
        alguna_coincidencia = False
        apellido_busqueda = input("Ingrese el apellido del participante que desea buscar: ")
        
        for i in range(len(array_nombres)):
            apellido = encontrar_apellido(array_nombres[i])
            contador_letra = 0
            bandera_coincidencia = False
            while contador_letra < len(apellido_busqueda) and contador_letra < len(apellido):
                if apellido[contador_letra] == apellido_busqueda[contador_letra]:
                    bandera_coincidencia = True
                    break
                contador_letra += 1
            if bandera_coincidencia == True:
                alguna_coincidencia = True
                mostrar_resultado(array_nombres, matriz_puntuaciones, i)
        if  alguna_coincidencia == False:
            print("No se encuentran coincidencias")
    else:
        retorno = False
        return retorno





def bubble_sort(arreglo:list) -> list:
    for i in range(len(arreglo) - 1):
        for j in range(i + 1, len(arreglo)):
            if arreglo[i] < arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
    return arreglo

array_nombres = ["pedro frachez","ana frank","juan roman","leo messi","mayra mendoza", " tanque silva"]
matriz_puntuaciones = [
    [10,7,7],
    [10,7,7],
    [6,5,5],
    [3,2,2],
    [5,3,3],
    [2,1,1],
]

array_para_ordenar = [47, 12, 89, 5, 73, 34, 21, 98, 66, 40]



