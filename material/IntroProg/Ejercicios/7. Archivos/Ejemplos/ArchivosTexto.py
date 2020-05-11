## Si no existe el archivo, lo crea y si ya existe lo reemplaza
def crearArchivo(path):
    archivo = open(path,"w")
    archivo.close()
    print("info: archivo creado con éxito\n")

def editarArchivo(path):
    lista = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    archivo = open(path,"a")
    for i in range(5):
        # SOLO RECIBE STR
        archivo.write(input("Digite un numero: ")+'\n')
    # archivo.write(lista) ( No funciona pq debe se una cadena)
    print("info: se ha escrito en el archivo correctamente \n")
    archivo.close()

def leerPrimeraLinea(path):
    archivo = open(path,"r")
    linea = archivo.readline()
    print("La primera linea del archivo tiene: ")
    print(linea)
    print("info: he terminado de leer el archivo \n")
    archivo.close()

def leerTodasLineas(path):
    archivo = open(path,"r")
    lista = []
    linea= None
    while linea!="":
        linea = archivo.readline()
        lista.append(linea)
    archivo.close()
    print(lista)
    print("info: He terminado de leer el archivo \n")

def main ():
    opc = 0
    #path ="../MisArchivos/Productos.txt"
    path ="Productos.txt"
    #path ="atletas.csv"
    while opc !=-1:
        print("Menu uso de archivos")
        opc=int(input("1. Crear un archivo \n2. Editar el archivo \n3. Leer primera linea \n4. Leer todas las lineas\n"))
        if opc == 1:
            crearArchivo(path)
        elif opc == 2:
            editarArchivo(path)
        elif opc == 3:
            leerPrimeraLinea(path)
        elif opc == 4:
            leerTodasLineas(path)

# LLamado principal
main()
    

