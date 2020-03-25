#Santiago Victori Diaz
def punto1():
    cont1=1
    conjuntos=int(input("ingrese el numero de conjuntos: "))
    while cont1<=conjuntos:
        apartamentos=int(input("cuantos apartamentos tiene el conjunto: "))
        cont2=1
        sumMas=0
        sumMas1=0
        while cont2<=apartamentos:
            mascotas=int(input("cuantas mascotas hay en el apartamento: "))
            sumMas1+=mascotas
            if mascotas>=3:
                sumMas+=1
            print("Apto", cont2, ": ", mascotas)
            cont2+=1
        print("el conjunto", cont1, "tiene", sumMas1, "mascotas")
        cont1+=1
    print("el numero total de apartamentos que tiene mas de 3 mascotas es: ", sumMas)

def punto2():
    cont1=1
    while cont1>0:
        num=int(input("ingrese un numero para sumar: ")
        suma=0
        contPeque=0
        while num not(==-1):
            if num%12==0:
                suma+=num
            elif num%9==0:
                suma1=suma*num
                suma+=suma1
            elif num%5==0:
                suma1=suma/5
                suma+=suma1
    print("el acumulado de las operaciones es: ", suma)



def f_calculoBase (km, tiemp, modalidad):
    if modalidad=="a la carta":
        valorBase=(km/100)*65000
    elif modalidad=="combo+":
        valorBase=(km/70)*25000+(tiemp/30)*10000
    elif modalidad=="combo++":
        valorBase=(km/50)*25000+(tiempo/60)*10000
    return valorBase

def f_costoAdicional(forPago, modalidad, numMaletas, tipVuelo, base):
    if forPago=="internet":
        descuento=(base*30)/1000
        adicion=descuento  #calcula mal el precio x internet
    elif modalidad=="a la carta" and tipVuelo=="nacional" and numMaletas>0:
        extra=numMaletas*70000
        adicion+=extra
    elif modalidad=="a la carta" and tipVuelo=="internacional" and numMaletas>0:
        extra=numMaletas*250000
        adicion+=extra        
    elif modalidad=="combo+" and tipVuelo=="nacional" and numMaletas>1:
        extraMaletas=numMaletas-1
        extra=extraMaletas*70000
        adicion+=extra        
    elif modalidad=="combo+" and tipVuelo=="internacional" and numMaletas>1:
        extraMaletas=numMaletas-1
        extra=extraMaletas*250000
        adicion+=extra
    elif modalidad=="combo++" and tipVuelo=="nacional" and numMaletas>2:
        extraMaletas=numMaletas-2
        extra=extraMaletas*70000
        adicion+=extra
    elif modalidad=="combo++" and tipVuelo=="internacional" and numMaletas>2:
        extraMaletas=numMaletas-2
        extra=extraMaletas*250000
        adicion+=extra
        return adicion

    def p_calculoTiquete(base, adicional):
        nombre=input("ingrese su nombre: ")
        km=float(input("ingrese los kilomatros que hay en su viaje: "))
        tiemp=int(input("ingrese el tiempo asignado para el viaje en minutos: "))
        modalidad=input("indique en que modalidad desea viajar, recuerde que tiene 3 opciones( a la carta, combo+ y combo++: ")
        forPago=input("ingrese la forma de pago")
        cantMaletas=int(input("ingrese el numero de maletas que desea llevar en la bodega: ")
        f_calculoBase(km, tiempo, modalidad)
        base=f_calculoBase(km, tiempo, modalidad)
        f_calculoAdicional(forPago, modalidad, cantMaletas, tipVuelo, base)
        adicional=f_calculoAdicional(forPago, modalidad, cantMaletas, tipVuelo, base)
        tiquete=base+adicional
        print("el señor", nombre, "tiene que pagar por su tiquete un total de: ", tiquete"

punto1():
punto2():
p_calculoTiquete(base, adicional):

              


          
    

            

            
    


