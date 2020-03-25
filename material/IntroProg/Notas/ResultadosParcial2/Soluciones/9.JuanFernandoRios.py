#Juan Fernando Rios Parcial 2
#Sección 1
def seccionUno():
    numConjuntos = int(input("¿Cuántos conjuntos van a ser encuestados? "))

    cont = 0
    while cont < numConjuntos:
        numApartamentos = int(input("¿Cuántos apartamentos tiene el conjunto? "))
        cont1 = 0
        numMascotas = 0
        dosMascotas = 0  # esto no se puede reiniciar aqui
        while cont1 < numApartamentos:
            mascotas = int(input("¿Cuántas mascotas viven en este apartamento? "))
            numMascotas = numMascotas + mascotas
            if mascotas == 2:
                dosMascotas += 1
            cont1+=1
        cont+=1
        print("El conjunto ", cont, "tiene ", numMascotas, "mascotas")
    if dosMascotas == 1:
        print("Hay",dosMascotas,"apartamento con 2 mascotas en total")
    else:
        print("Hay",dosMascotas,"apartamentos con 2 mascotas en total")

#Sección 2
def seccionDos():
     

    num = 0
    acumulado = 0
    primera = False
    while num != -1:
        num = int(input("Ingrese un número entero "))
        if acumulado == 0:
            acumulado = num
        else:
            if num%8==0:
                acumulado += num
            elif num %9==0:
                acumulado = acumulado*num
            elif num%7==0:
                acumulado = acumulado-num
            elif num%5==0:
                acumulado = acumulado / num
        if primera == False:
            minimo = num
            primera = True
        else:
            if minimo > num and num!=-1:
                minimo = num

    print("El acumulado es: ", acumulado)
    print("El mínimo es: ", minimo)



#Seccion 3
def f_calculoBase(km,tiempo,tiquete):
    if tiquete == 1: #a la carta
        vBase = (km/100)*55000
    elif tiquete == 2: # combo+
        vBase = (km/70)*25000+(tiempo/30)*10000
    elif tiquete == 3: # combo++
        vBase = (km/50)*25000+(tiempo/60)*10000
    return vBase

def f_costoAdicional(formaPago,tiquete,maletas,tipoVuelo):
    if tipoVuelo == "NACIONAL":
        pMaleta = 70000
    else:
        pMaleta = 250000
    
    if formaPago == "INTERNET":
        descuento = 0.7
    else:
        descuento = 1
        
    if tiquete == 1: #a la carta
        vAdicional = descuento*(maletas*pMaleta)
    elif tiquete == 2: # combo+
        if maletas <= 1:
            vAdicional = 0
        else:
            vAdicional = descuento*((maletas-1)*pMaleta)
    elif tiquete == 3: # combo++
        if maletas <= 2:
             vAdicional = 0
        else:
            vAdicional = descuento*((maletas-2)*pMaleta)
    return vAdicional

def p_calculoTiquete():
    nombre = input("Ingrese el nombre del pasajero ")
    tiquete = int(input("Elija su modalidad de vuelo 1.A LA CARTA  2.COMBO+  3.COMBO++ "))
    tipoVuelo = input("Es un vuelo nacional o internacional (Escriba NACIONAL o INTERNACIONAL) ").upper()
    km = float(input("¿Cuántos kilometros tiene su vuelo "))
    tiempo = float(input("¿Cuál es la duración en minutos de su vuelo? "))
    maletas = int(input("¿Cuantas maletas llevará por bodega? "))
    formaPago = input("¿Realizará el pago por internet? (Escriba INTERNET o NORMAL) ").upper()
    vFinal = (f_calculoBase(km,tiempo,tiquete)+f_costoAdicional(formaPago,tiquete,maletas,tipoVuelo))
    print ("El precio total del vuelo es de :",vFinal)



seccionUno()
seccionDos()
p_calculoTiquete()

                    
        
