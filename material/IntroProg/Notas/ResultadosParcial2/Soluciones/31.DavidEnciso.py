
pregunta=int(input("Ingrese la pregunta que quiere ver: "))
if pregunta==1:
    examen(num1)
if pregunta==2:
    examen(num2)
def examen(num1):
    N = int(int(input("Ingresar número de conjuntos residenciales: ")))
    M = int(input("Ingresar número de apartamentos: "))
    cont = 0
    contmascota = 0
    ceromascota = 0
    while (cont < N):
        cont += 1
        cont1 = 0
        cont2 = 0
        cont3 = 0
        contmascota = 0
        while (cont1 < M):
            cont1 += 1
            mascota = int(input("Ingrese el número de mascotas que tiene: "))
            contmascota = mascota + contmascota
        if mascota == 0:
            ceromascota = +1
        while (cont2 < 1):
            cont2 = +1
            print("El numero total de mascotas en el conjunto", cont3, "es: ", contmascota)
    print("El numero de aprtamentos que no tiene mascotas es: ", ceromascota)
def examen(num2):
    acumulado = 0
    while (numero != -1):
        numero = int(input("Ingrese un número: "))
        while (numero < -1):
            numero = int(input("Ingrese un valor correcto"))
        if numero % 4 == 0:
            acumulado = numero + acumulado
            print(acumulado)
        elif numero % 9 == 0:
            acumulado = numero * acumulado
            print(acumulado)
        elif numero % 7 == 0:
            acumulado = numero - acumulado
            print(acumulado)
        elif numero % 5 == 0:
            acumulado = acumulado / 5
            print(acumulado)
        elif numero == -1:
            print(acumulado)
def examen(num3):
    def f_calculoBase(var1):
        print("A la carta: 1")
        print("Combo+: 2")
        print("Combo++: 3")
        tipovuelo = int(input("Ingrese el tipo de vuelo que va hacer:"))
        km = int(input("Ingrese la distancia: "))
        tiempo=int(input("Ingrese tiempo de vuelo en minutos:"))
        tiempo1=tiempo/30
        tiempo2=tiempo/60
        km1=km/100
        km2=km/70
        km3=km/50
        if tipovuelo == 1:
            valortiqueteinicial = 35000*km1
            return valortiqueteinicial
        if tipovuelo == 2:
            valortiqueteinicial = 25000*km2+(tiempo1*10000)
            return valortiqueteinicial
        if tipovuelo == 3:
            valortiqueteinicial = 25000*km3+(tiempo2*10000)
            return valortiqueteinicial
    valorbase=f_calculoBase(var1)

    def f_costoAdicional(var1):
        print("A la carta: 1")
        print("Combo+: 2")
        print("Combo++: 3")
        valoradiconal=0
        tipovuelo = int(input("Ingrese el tipo de vuelo que va hacer:"))
        formadepago=input("Ingrese la forma de pago")
        cantidadm=int(input("Ingrese la cantidad maletas que vas a ingresar a la bodega: "))
        tipo2=input("Ingrese el tipo de trayecto que va a hacer: ")
        if tipovuelo == 1 and tipo2==nacional and cantidadm>0:
            valoradicional= valoradicional+(cantidadm*70000)
            return valortiqueteinicial
        if tipovuelo == 1 and tipo2 == internacional and cantidadm > 0:
            valoradicional = valoradicional + (cantidadm * 25000)
            return valortiqueteinicial
        if tipovuelo == 2 and tipo2==nacional and cantidadm>1:
            valoradicional= valoradicional+(cantidadm*70000)
            return valortiqueteinicial
        if tipovuelo == 2 and tipo2 == internacional and cantidadm > 1:
            valoradicional = valoradicional + (cantidadm * 25000)
            return valortiqueteinicial
        if tipovuelo == 3 and tipo2==nacional and cantidadm>2:
            valoradicional= valoradicional+(cantidadm*70000)
            return valortiqueteinicial
        if tipovuelo == 3 and tipo2 == internacional and cantidadm >2:
            valoradicional = valoradicional + (cantidadm * 25000)
            return valortiqueteinicial
    valoradicional=f_costoAdicional(var1)
     def p_calculoTiquete(var):
        nombre=input("Ingrese su nombre")
        valorfinal=valorbase+valoradicional
        print("nombre")
        return valorfinal
     final=p_calculoTiquete
     print(final)


