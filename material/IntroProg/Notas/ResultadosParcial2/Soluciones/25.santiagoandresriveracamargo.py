#Santiago Andrés Rivera Camargo
def mascotas():
    valorN=int(input("número de conjuntos residenciales"))
    cont=0
    while cont<valorN:
        valorM=int(input("número de apartamentos"))
        cont1=0
        suma=0
        suma1=0
        while cont1<valorM:
            nMascotas=int(input("numero de mascotas"))
            cont1+=1
            suma+=nMascotas
            if cont1>=3:
                suma1+=cont1
        print("el conjunto tiene",suma,"mascotas")
        cont+=1
        print("número de conjuntos con mas o tres mascotas",suma1)

def calculadora():
    cont=0
    acum=0
    entrante=0
    bandera=1
    menor=0
    acum1=0
    while entrante!=-1:
        entrante=int(input("número entrante"))
        if entrante%1==0:
            acum+=entrante
        if entrante%12==0:
            acum+=entrante
        if entrante%9==0:
            acum*=entrante
        if entrante%7==0:
            acum-=entrante
        if entrante%5==0:
            acum=acum/entrante
        print(acum)
        acum+=entrante
    cont+=1
    if bandera==1:  # Esta donde no es
        num=menor
        bandera=2
    elif num<menor:
        menor=num
    print("el número menor es:",menor)

def f_calculoBase(distancia,minutos,modalidad):
    if modalidad=="a la carta":
        valorBase=(distancia/100)*65000
    elif modalidad=="combo+":
        valorBase=(distancia/70)*25000+(minutos/30)*10000
    elif modalidad=="combo++":
        valorBase=(distancia/50)*25000+(minutos/60)*10000
    return valorBase

def f_costoAdicional(pago,modalidad,maletas,tipov):
    if pago=="internet":
        if tipov=="nacional":
            valorAdicional=0.7*(maletas*70000)
        elif tipov=="internacional":
            valorAdicional=0.7*(maletas*250000)
    else:
        if tipov=="nacional":
            valorAdicional=maletas*70000
        elif tipov=="internacional":
            valorAdicional=maletas*250000
    return valorAdicional

def p_calculoTiquete():
    nombreC=input("nombre del cliente")
    distancia=int(input("distancia hasta el destino"))
    minutos=int(input("minutos que demora el vuelo"))
    modalidad=input("modalidad: a la carta, combo+, combo++")
    pago=input("internet o normal")
    maletas=int(input("número de maletas"))
    tipov=input("nacional o internacional")
    # Es + el costo adicional
    valorfinal=f_calculoBase(distancia,minutos,modalidad)-f_costoAdicional(pago,modalidad,maletas,tipov)
    print(nombreC)
    print(valorfinal)
    

print("escoja opcion 1=mascotas 2=multicalculadora 3=vivair")
num=int(input("ingrese opcion"))
if num==1:
    mascotas()
elif num==2:
    calculadora()
elif num==3:
    p_calculoTiquete()
else:
    print("no existe esa opción")
