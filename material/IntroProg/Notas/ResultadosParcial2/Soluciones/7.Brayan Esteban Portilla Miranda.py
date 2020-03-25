#Brayan Esteban Portilla Miranda
def HMascotas (conjuntosR):
    conjuntosR=int(input("Conjuntos residenciales: "))
    cont=0
    dosMascotas=0
    while cont<conjuntosR:
        apartamentos=int(input("numero de apartamentos en este conjunto: "))
        contApa=0
        suma=0
        while contApa<apartamentos:
            mascotas=int(input("¿Cuantas Mascotas tiene?: "))
            suma=suma+mascotas
            if mascotas==2:
                dosMascotas=dosMascotas+1
            contApa=contApa+1
        print("Este conjunto tiene",suma,"Mascotas")
        cont=cont+1
    print(dosMascotas,"Apartamentos tienen 2 mascotas")
def MultiCalculadora():
    num=0
    acumulado=0
    while num!=-1:
        num=int(input("Ingrese el número: "))
        if acumulado==0:
            acumulado=acumulado+num
        else:
            if num%8==0:
                acumulado=acumulado+num
            elif num%9==0:
                acumulado=acumulado*num
            elif num%7==0:
                acumulado=acumulado-num
            elif num%5==0:
                acumulado=acumulado/5
            else:
                acumulado=acumulado
    print(acumulado)
def f_calculoBase(distancia,TVuelo,modalidad):
    if modalidad==1:
        valorBase=(distancia/100)*55000
    elif modalidad==2:
        valorBase=(distancia/70)*25000+(TVuelo/30)*10000
    elif modalidad==3:
        valorBase=(distancia/50)*25000+(TVuelo/60)*10000
    return valorBase
def f_costoAdicional(fPago,modalidad,cantMaletas,tipoVuelo):
    if fPago==1:
        if modalidad==1:
            valorAdicional=cantMaletas*tipoVuelo
        elif modalidad==2:
            valorAdicional=(cantMaletas-1)*tipoVuelo
        elif modalidad==3:
            valorAdicional=(cantMaletas-2)*tipoVuelo
    else:
        if modalidad==1:
            valorAdicional=0.7*(cantMaletas*tipoVuelo)
        elif modalidad==2:
            valorAdicional=0.7*((cantMaletas-1)*tipoVuelo)
        elif modalidad==3:
            valorAdicional=0.7*((cantMaletas-2)*tipoVuelo)
    return valorAdicional
nombre=input("Ingrese el nombre del cliente: ")
modalidad=int(input("Si la modalidad del tiquete es a la carta ingrese <1>, si es Combo+ ingrese <2> y si es Combo++ ingrese <3>: "))
if modalidad != 1:
    TVuelo = int(input("Ingrese el tiempo en minutos que demora el vuelo: "))
else:
    TVuelo=0
distancia=int(input("Ingrese la distancia del vuelo en Km: "))
fPago=int(input("Si la forma de pago es por internet digite <2>, de lo contrario digite <1>: "))
cantMaletas=int(input("Ingrese la cantidad de maletas que iran en bodega: "))
tipo=int(input("Si el vuelo es nacional digite <1>, si el vuelo es internacional digite <2>: "))
if tipo==1:
    tipoVuelo=70000
else:
    tipoVuelo=250000
VFinal=int(f_calculoBase(distancia,TVuelo,modalidad)+f_costoAdicional(fPago,modalidad,cantMaletas,tipoVuelo))
print(nombre,VFinal)


HMascotas(conjuntosR)
MultiCalculadora(num)
