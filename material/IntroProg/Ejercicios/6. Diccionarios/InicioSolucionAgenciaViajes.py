
def ejemplos(viajesDic):
    cantElem = len(viajesDic)
    maxValor= 2500000  # Numeros magicos.. mala práctica de programación
    for i in range (cantElem):
        datosXDestino = viajesDic[i]
        # print (viajesDic[i])
        #print("IncluyeGuia", datosXDestino['IncluyeGuia'])
        # Version mejorada
        #print("IncluyeGuia", datosXDestino.get('IncluyeGuia'))
        if datosXDestino.get('IncluyeGuia') == None:
            print ("El paquete no tiene guía turístico")
        if datosXDestino.get('precioPersona') > maxValor:
            print("Destino ", i + 1)
            print("Destino: ", datosXDestino['destino'])
            print("PrecioxPersona: ", datosXDestino['precioPersona'])

        # Actualizar para el hotel blue reef precio de 4000000
        if datosXDestino.get('hotel') == 'Blue Reef':
            viajesDic[i]['precioPersona'] = 4000000

def imprimirDestinos(viajesDic):
    cantElem = len(viajesDic)
    maxValor= 2500000  # Numeros magicos.. mala práctica de programación
    for i in range (cantElem):
        datosXDestino = viajesDic[i]
        print("Destino ", i + 1)
        print("Destino: ", datosXDestino['destino'])
        print("PrecioxPersona: ", datosXDestino['precioPersona'])
print("hola 'luisa' ")

""" 
Recibe la lista de diccionarios de viajes y un destino. 
Retorna sublistas con el nombre del hotel y la tarifa por persona de los paquetes que 
cumplan con el destino. 
Ejemplo. Si se recibe la lista de diccionarios de viajes del ejemplo 
"""
def recomendarHotelxDestino(viajes, destino):
    listaGeneral = []
    for i in range(len(viajes)):
        datosXdestino = viajes[i]
        if datosXdestino['destino'] == destino:
            listaPequenia = []
            listaPequenia.append(datosXdestino['hotel'])
            listaPequenia.append(datosXdestino['precioPersona'])
            listaGeneral.append(listaPequenia)
           ## otra opcion
            #listaGeneral.append([datosXdestino['hotel'], datosXdestino['precioPersona']])
    return listaGeneral

"""
b)	Función recomendarPorPrecio: dada una lista de diccionarios de viajes y 
un valor de pago por persona 
retorna sublistas con el nombre del hotel y la tarifa por persona 
de los paquetes que cumplan con el valor definido teniendo en cuenta 
el descuento del paquete turístico.  Ejemplo. Si se recibe la lista de listas de 
viajes del ejemplo y el valor 1500000 el resultado sería 
[['Sol Caribe', 1500000]], ['Mar y Sol', 1300000] ]. 
"""
def recomendarHotelxPrecio(viajes, valorMaximo):
    listaGeneral = []
    for i in range(len(viajes)):
        datosXdestino = viajes[i]
        valorPaquete = datosXdestino['precioPersona']
        porcDescuento = datosXdestino['descuento'] / 100
        valorDescuento = (valorPaquete * porcDescuento)
        valorNeto = valorPaquete - valorDescuento
        if valorNeto <= valorMaximo:
            listaPequenia = []
            listaPequenia.append(datosXdestino['hotel'])
            listaPequenia.append(datosXdestino['precioPersona'])
            # A manera de información incorporo el valor neto
            listaPequenia.append({'valorNeto': valorNeto})
            listaGeneral.append(listaPequenia)
    return listaGeneral


def menu ():
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

    opc = 0
    while ( opc != -1):
        print ("Hola que quieres hacer :")
        print (" 1. Imprimir todos los destinos: ")
        print(" 2. Recomendar x destino: ")
        print(" 3. Recomendar x precio: ")
        print ("-1. Salir ")
        opc = int(input(""))

        # Opciones
        if opc == 1:
            imprimirDestinos(viajes)
        if opc == 2:
            destino = input("Ingrese el destino")
            listaRecomendados=recomendarHotelxDestino(viajes, destino)
            print(listaRecomendados)
        if opc == 3:
            precio = int(input("Ingrese el precio máximo"))
            listaRecomendados = recomendarHotelxPrecio(viajes, precio)
            print(listaRecomendados)
# LLamado principal
menu()