## Escribir y leer archivo de forma binaria

import marshal

def guardarBinarios(path, data):
    file = open(path, "bw")
    marshal.dump(data, file)
    file.close()

def leerBinarios(path):
    # Se ajusta para que no muera cuando el archivo no existe
    try:
        file = open(path, "br")
        datosCargados = marshal.load(file)
        file.close()
        # Si tiene datos los retorna
        return datosCargados
    except:
        return None  # Esto indica que no hay nada para leer

def agregarListaBinaria(path, data):
    file = open(path, "br")
    data = marshal.load(file)
    file.close()
    for i in range(3):
        data.append(input("Digite un numero: "))

    #Se guardan los datos
    guardarBinarios(path, data)

def agregarDatosDiccionario(diccionario):
    novio= input("Tienes novio? ")
    diccionario['novio']= novio
    esVegetariana = input("Eres vegetariana ? ")
    diccionario['vegetariana'] = esVegetariana
    return diccionario

def imprimirDiccionario(diccionario):
    # Imprimo el diccionario elemento x elemento ( pq asi lo pidio brayan).
    #for key in diccionario:
        #print(key, ":", diccionario[key])
    print ('hobbies:', diccionario['hobbies'] )


def imprimirMatriz():
    matrizImprimir = [[1,2,3], [4,5,6], [7,8,9]]
    for fila in matrizImprimir:
        print("\t\t\t\t",fila)

def agregarHobbie(diccionario):
    #Si ya existe el campo hobbies en el diccionario
    if diccionario.get('hobbies')!= None:
        diccionario.get('hobbies').append(input("Dime otro hobbie"))
    else:
        diccionario['hobbies'] = []
        hobbie= input("Dime un hobbie")
        diccionario['hobbies'].append(hobbie)
    return diccionario

def existenDatos(diccionario):
    if diccionario.get('tablero') == None:
        return False
    else:
        return True

def mainJuego():
    print("Opciones")
    print("1. Iniciar juego \n"
          "2. Imprimir matriz \n");
    opc = int(input(""));
    # Diccionario vacio
    datosJuego ={}
    path ="datos.minas"
    if opc == 1:
        datosJuego = leerBinarios(path)
        if datosJuego != None:
            print("Existia algo ")
        else:
            #NO existen datos entonces inicio todo
            # Se inicia el tablero, las minas, las vidas
            print(" No existe el archivo entoncces  voy a hacer el inicio de todo ")
    elif opc == 2:
        imprimirMatriz()



def main ():
    opc = 0
    lista = [1, 2, 3, 4]
    viajes = [{'destino': 'San Andres', 'precioPersona': 2000000, 'hotel': 'Blue Reef', 'descuento': 20,
               'tipoPaquete': 'Todo Incluido', 'incluyeVuelo': True},
              {'destino': 'Cartagena', 'precioPersona': 1500000, 'hotel': 'Sol Caribe', 'descuento': 0,
               'tipoPaquete': 'Hospedaje', 'incluyeVuelo': False},
              {'destino': 'Santa Marta', 'precioPersona': 1300000, 'hotel': 'Mar y Sol', 'descuento': 10,
               'tipoPaquete': 'Todo Incluido', 'incluyeVuelo': False},
              {'destino': 'San Andres', 'precioPersona': 3000000, 'hotel': 'El Dorado', 'descuento': 5,
               'tipoPaquete': 'Hospedaje', 'incluyeVuelo': True},
              {'destino': 'Cartagena', 'precioPersona': 2100000, 'hotel': 'Decameron', 'descuento': 5,
               'tipoPaquete': 'Hospedaje', 'incluyeVuelo': False},
              {'destino': 'Cartagena', 'precioPersona': 1800000, 'hotel': 'El dorado', 'descuento': 0,
               'tipoPaquete': 'Hospedaje', 'incluyeVuelo': True},
              {'destino': 'Cartagena', 'precioPersona': 2500000, 'hotel': 'Hilton', 'descuento': 25,
               'tipoPaquete': 'Hospedaje', 'incluyeVuelo': True}]
    #path ="../MisArchivos/Productos.dat"
    path ="datos.valeria"
    while opc !=-1:
        print("Menu uso de archivos binarios")
        opc=int(input("1. guardar binario( lista) \n2. Leer binario (lista) \n"
                      "3. guardar binario(lo del valeria) \n4. Leer binario(lo de valeria)\n"
                      "5. Agregar a lista binaria\n 6. Agregar datos personales  a dicc valeria \n"
                      "7. Imprimir diccionario \n  8.Agregar hobbies \n"))
        if opc == 1:
            guardarBinarios(path, lista)
        elif opc == 2:
            datosArchivo=leerBinarios(path, lista)
        elif opc == 3:
            diccionario = {"edad":17, "genero": "femenino", "hobbies": ["ejercicio", "dibujar"] }
            guardarBinarios(path, diccionario)
        elif opc == 4:
            datosArchivo=leerBinarios(path)
            print("Lo que tenía el archivo de valeria")
            print(datosArchivo)
        elif opc == 5:
            agregarListaBinaria(path, lista)
        elif opc == 6:
            # Leeo lo que esta actualmente en el diccionario y lo guardo en una diccionario en memoria
            diccionario = leerBinarios(path)
            # Le agrego datos al diccionario en memoria
            diccionarioModificado=agregarDatosDiccionario(diccionario)
            # Guardo el nuevo diccionario en el archivo ( con los cambios), lo reemplazo
            guardarBinarios(path, diccionarioModificado)
            # Verificó al volver a leer que los cambios hubieran quedado bn
            print("Verifico si hubo cambios")
            diccionario = leerBinarios(path)
            imprimirDiccionario(diccionario)
        elif opc == 7:
            # Leeo lo que esta actualmente en el diccionario y lo guardo en una diccionario en memoria
            diccionario = leerBinarios(path)
            imprimirDiccionario(diccionario)
        elif opc == 8:
            # Leo el diccionario
            diccionario = leerBinarios(path)
            # Agregar hobbie
            diccionarioModificado = agregarHobbie(diccionario)
            # Guardo el cambio
            guardarBinarios(path,diccionarioModificado)
            print ("Se agrego un hobbie con exito")

# LLamado principal
#main()
mainJuego()