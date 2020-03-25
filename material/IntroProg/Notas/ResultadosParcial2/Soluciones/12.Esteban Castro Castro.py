#Esteban Castro
#secciónUno
def pets():
    cantMasc=int(input("Cantidad de mascotas en el apto: "))
    return cantMasc
def seccionUno():
    conjuntos=int(input("Cantidad de conjuntos: "))
    mascoPorConj=0
    conjuntoNum=0
    while conjuntos > 0:
        conjuntos-=1
        conjuntoNum+=1
        apartamentos=int(input("Cantidad de apartamentos: "))
        aptoConM=0
        while apartamentos > 0:
            apartamentos-=1
            mascotas=pets()
            mascoPorConj+=mascotas
            if mascotas>0:
                aptoConM+=1
        if aptoConM>0:
            print("El total de apartamentos con mascotas es:",aptoConM)
    # Esto debería haber ido en el while de adentro
    print("El conjunto #",conjuntoNum,"Tiene un total de",mascoPorConj,"mascotas")
seccionUno()

#secciónDos
def mult6(num,acumulado):
    acumulado+=num
    return acumulado

def mult9(num,acumulado):
    acumulado*=num
    return acumulado

def mult7(num,acumulado):
    acumulado-=num
    return acumulado

def mult5(num,acumulado):
    acumulado= acumulado/num
    return acumulado


def seccionDos():
    menor=0
    opera=0
    primerMenor=True
    acumulado=0
    num=0
    while num != -1:
        num=int(input("Ingrese un número para la calculadora: "))
        if num==0:
            acumulado=0
        if primerMenor==True:
            menor=num
            primerMenor=False
        if num < menor and num !=-1:
            menor=num
        if num%6==0:
            opera= mult6(num,acumulado)
            acumulado=opera
        elif num%9==0:
            opera= mult9(num,acumulado)
            acumulado=opera
        elif num%7==0:
            opera= mult7(num,acumulado)
            acumulado=opera
        elif num%5==0:
            opera=mult5(num,acumulado)
            acumulado=opera
    if num==-1:
        primer=False
    print("El resultado de la calculadora es: ",acumulado)
    print("El menor número ingresado por el usuario fue:",menor)

seccionDos()

#secciónTres
def calculoBase(modalidad, distancia, tiempo):
    valorBase=0
    if modalidad==1:
        valorBase=(distancia/100)*45000
    elif modalidad==2:
        valorBase=(distancia/70)*25000+ (tiempo/30)*10000
    elif modalidad==3:
        valorBase=(distancia/50)*25000+ (tiempo/60)*10000
    return valorBase

def costoAdicional(modoPago,modalidad,maletas,vuelo):
    valorAdicional=0
    valorFinal=0
    if modalidad==1:
        if vuelo ==1:#vuelo nacional
            valorAdicional+=(maletas*70000)
        else: #vuelo internacional
            valorAdicional+=(maletas*250000)
        
    elif modalidad==2:
        if vuelo==1: #vuelo nacional
            if maletas > 1:
                valorAdicional+=((maletas-1)*70000)
        else: #vuelo internacional
            if maletas > 1:
                valorAdicional+=((maletas-1)*250000)
                
    elif modalidad==3:
        if vuelo==1: #vuelo nacional
            if maletas > 2:
                valorAdicional+=((maletas-2)*70000)
        else: #vuelo internacional
            if maletas > 2:
                valorAdicional+=((maletas-2)*250000)
    
    if modoPago == 1: #pagado por internet
            valorFinal= 0.7*valorAdicional
    return valorFinal

def procedimiento():
    nombre=input("Ingrese el nombre del cliente: ")
    print("1. A la carta \n2. Combo+ \n3. Combo++")
    modalidad=int(input("Ingrese un número para la modalidad que desea: "))
     
    distancia=int(input("Cantidad de distancia (en kilometros): "))
    tiempo=int(input("Cantidad de tiempo (en minutos): "))
    precioBase= calculoBase(modalidad, distancia, tiempo)
    print("¿Cómo pagó su tiquete?")
    modoPago=int(input("1. Internet \n2. normal\n"))
    maletas=int(input("Cantidad de maletas en bodega que desea llevar: "))
    print("¿Qué tipo de vuelo es?")
    vuelo=int(input("1. Nacional \n2. Internacional\n"))
    precioAdicional= costoAdicional(modoPago,modalidad,maletas,vuelo)
    
    total=precioBase+precioAdicional
    print("El cliente:",nombre,"\nDebe pagar por su tiquete:",total)
    
procedimiento()












