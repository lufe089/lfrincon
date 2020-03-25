#César Manuel Samboni Rojas
#ejercicio 1
def Sondeo():
    conjuntos= int (input("ingrese cuantos conujntos realizaran la encuesta: "))
    apartamentos= int (input("ingrese cuantos apartamentos tiene cada conjunto: "))
    mascotasT=0
    SinMascotas=0
    cont3= 1
    while conjuntos > 0:
        mascotas1=0
        cont=1
        cont2=0
        while cont2 < apartamentos:
            print(" el apartamento", cont)
            mascotas= int (input("cuantas mascotas tiene? "))
            if mascotas == 0:
                SinMascotas+=1
            mascotas1+=mascotas
            cont+=1
            cont2+=1
        print ("los apartamentos que tiene 0 mascotas son", SinMascotas)
        mascotasT+=mascotas1
        print ("el conjunto", cont3, "tiene", mascotasT, "mascotas")  
        conjuntos-=1
        cont3+=1
#ejercicio 2

def MultiCalculadora():
    acumulado = 0
    númeroEntrante= int (input("ingrese un número que la MultiCalculadora tomará "))
    acumulado+=númeroEntrante
    númeroMenor= 0
    print("su resultado es", acumulado)
    while númeroEntrante!=-1:
        númeroEntrante= int (input("ingrese un número que la MultiCalculadora tomará "))
        if númeroEntrante%4==0:
            acumulado+=númeroEntrante
            print("su resultado es", acumulado)
        elif númeroEntrante%9==0:
            acumulado*=númeroEntrante
            print("su resultado es", acumulado)
        elif númeroEntrante%7==0:
            acumulado-=númeroEntrante
            print("su resultado es", acumulado)
        elif númeroEntrante%5==0:
            acumulado/=númeroEntrante
            print("su resultado es", acumulado)
        elif númeroEntrante==-1:
            print("gracias por usar la MultiCalculadora, hasta la próxima")
        else:
            print("como el número no cumple ninguna regla, el resultado es", acumulado)
        if númeroEntrante < númeroMenor:
            númeroMenor=númeroEntrante       
    print ("el número menor ingresado fue:", númeroMenor)

#ejercicio 3
def calculoBase(D, Min, Modo):
    if Modo==1:
        valorBase= (D/100)*35000
    elif Modo==2:
        valorBase= (D/70)*25000+(Min/30)*10000
    elif Modo==3:
        valorBase= (D/50)*25000+(Min/60)*10000
    return valorBase

def CostoAdicional (Fpago, Modo, Maletas, Tvuelo):
    if Tvuelo==1:
        if Fpago==1:
            if Modo==1:
                ValorAdicional= 0.7*(Maletas*70000)
            elif Modo==2:
                ValorAdicional= 0.7*((maletas-1)*70000)
            elif Modo==2:
                ValorAdicional= 0.7*((maletas-2)*70000)
        elif Fpago==2:
            if Modo==1:
                ValorAdicional=(Maletas*70000)
            elif Modo==2:
                ValorAdicional=((maletas-1)*70000)
            elif Modo==2:
                ValorAdicional=((maletas-2)*70000)
    elif Tvuelo==2:
        if Fpago==1:
            if Modo==1:
                ValorAdicional= 0.7*(Maletas*250000)
            elif Modo==2:
                ValorAdicional= 0.7*((maletas-1)*250000)
            elif Modo==2:
                ValorAdicional= 0.7*((maletas-2)*250000)
        elif Fpago==2:
            if Modo==1:
                ValorAdicional=(Maletas*250000)
            elif Modo==2:
                ValorAdicional=((maletas-1)*250000)
            elif Modo==2:
                ValorAdicional=((maletas-2)*250000)
    return ValorAdicional

def CalculoTiquete(D, Min, Modo, Fpago, Maletas, Tvuelo):
    ValorBase=calculoBase(D,Min,Modo)
    print ("el valor base es", ValorBase)
    CostoA=CostoAdicional (Fpago, Modo, Maletas, Tvuelo)
    print ("el costoAdicional es", CostoA)
    CostoFinal= ValorBase+CostoA
    return CostoFinal

def VivaAir():
    nombre = input ("ingrese su nombre: ")
    D= int (input("ingrese la Distancia del destino: "))
    Min= int (input("ingrese los minutos que durará el viaje: "))
    Modo=int (input("seleccione su modo: 1. a la carta. 2.Combo + 3.Combo++: "))
    Fpago= int (input("seleccione su forma de pago: 1. internet 2.normal "))
    Maletas= int (input ("ingrese la cantidad de maletas que quiere llevar en la bodega: "))
    Tvuelo= int (input ("seleccione el tipo de vuelo 1. nacional. 2.internacional "))
    CostF=CalculoTiquete(D, Min, Modo, Fpago, Maletas, Tvuelo)
    print (nombre, "el valor final a pagar es", CostF)

sondeo()
MultiCalculadora()
VivaAir()

    
    

        
        
