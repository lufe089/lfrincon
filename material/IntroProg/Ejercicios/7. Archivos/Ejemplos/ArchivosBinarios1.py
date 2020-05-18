## Escribir y leer archivo de forma binaria

import marshal

def guardarBinarios(path, data):
    file = open(path, "bw")
    marshal.dump(data, file)
    file.close()

def leerBinarios(path, data):
    file = open(path, "br")
    dataLoad = marshal.load(file)
    print("Deserializado binario", dataLoad)
    file.close()

def agregarListaBinaria(path, data):
    file = open(path, "br")
    data = marshal.load(file)
    file.close()
    for i in range(3):
        # SOLO RECIBE STR
        data.append(input("Digite un numero: "))

    #Se guardan los datos
    guardarBinarios(path, data)

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
    path ="Productos1.dat"
    while opc !=-1:
        print("Menu uso de archivos binarios")
        opc=int(input("1. guardar binario( lista) \n2. Leer binario (lista) \n"
                      "3. guardar binario(diccionario) \n4. Leer binario(diccionario)\n"
                      "5. Agregar a lista binaria\n"))
        if opc == 1:
            guardarBinarios(path, lista)
        elif opc == 2:
            leerBinarios(path, lista)
        elif opc == 3:
            guardarBinarios(path, viajes)
        elif opc == 4:
            leerBinarios(path, viajes)
        elif opc == 5:
            agregarListaBinaria(path, lista)

# LLamado principal
main()