def cargar_clasificaciones(matriz_votos:list,array_nombres:list) -> bool:
    retorno = False
    
    if type(matriz_votos) == list and len(matriz_votos) > 0 and type(array_nombres) == list and len(array_nombres) > 0:
        for fil in range(len(matriz_votos)):
            if type(matriz_votos[fil]) == list:
                for col in range(len(matriz_votos[fil])):
                    print(f"Cargando clasificacion juez {array_nombres[fil]}")
                    clasificacion_juez = input(f"Ingrese la clasificacion del juez {col + 1}: ")
                    clasificacion_valida = verificar_clasificacion (clasificacion_juez,f"Reingrese la clasificacion del juez {col + 1}: ", "Clasificacion no valida" )
                    matriz_votos[fil][col] = clasificacion_valida
                    retorno = True
    
    return retorno


def Validar_ingreso_clasificaciones(numero_a_validar: str) -> bool:
    retorno = True
    if len(numero_a_validar) == 0 or numero_a_validar == "-0":
        retorno = False
    for i in range(len(numero_a_validar)):
        valor_a_comparar = ord(numero_a_validar[i])
        if valor_a_comparar < 48 or valor_a_comparar > 57:
            retorno =  False
            break
        else:
            numero_a_validar = int(numero_a_validar)
            if numero_a_validar >10:
                retorno = False
    return retorno 

def verificar_clasificacion(numero:str, mensaje_reingreso:str, mensaje_error:str) -> int|float:
    while Validar_ingreso_clasificaciones(numero) == False:
        print(f"{mensaje_error}")
        numero = input(f"{mensaje_reingreso}")
        
    numero = int(numero)
    return numero


def cargar_nombres(array_nombres:list) -> bool:
    if type(array_nombres) == list and len(array_nombres) > 0:
        for i in range(len(array_nombres)):
            nombre_participante = input(f"Ingrese el nombre del participante {i + 1}: ")
            nombre_participante = verificar_ingreso_nombre(nombre_participante,f"Reingrese el nombre del participante {i + 1}: ","Nombre no valido")
            array_nombres[i] = nombre_participante

        return True
    else:
        return False


def Validar_ingreso_nombre(cadena: str) -> bool:
    if len(cadena) <= 2:
        return False

    cantidad_espacios = 0
    posicion_espacio = 0
    retorno = True

    for i in range(len(cadena)):
        valor_a_comparar = ord(cadena[i])
        if valor_a_comparar >= 65 and valor_a_comparar <= 90:
            retorno = True 
        elif valor_a_comparar >= 97 and valor_a_comparar <= 122:
            retorno = True 
        elif valor_a_comparar == 32:
            if cantidad_espacios == 0:
                if i >= 3 and (len(cadena) - i - 1) >= 3:
                    cantidad_espacios = cantidad_espacios + 1
                    posicion_espacio = i
                    retorno = True
                else:
                    retorno = False
            else:
                retorno = False  
        else:
            retorno = False
        if retorno == False:
            break


    longitud_nombre = posicion_espacio
    longitud_apellido = len(cadena) - posicion_espacio - 1

    if cantidad_espacios != 1:
        retorno = False
    elif longitud_nombre < 3:
        retorno = False
    elif longitud_apellido < 3:
        retorno = False

    return retorno

def verificar_ingreso_nombre(cadena:str, mensaje_reingreso:str, mensaje_error:str) -> str:
    while Validar_ingreso_nombre(cadena) == False:
        print(f"{mensaje_error}")
        cadena = input(f"{mensaje_reingreso}")
    return cadena


