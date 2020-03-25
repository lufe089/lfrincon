#Manuela Zuluaga Aristizabal
def sondeoHospitalMascotas():
    M=int(input("Conjuntos residenciales a encuestar: "))
    N=int(input("Apartamentos por conjunto: "))
    cont=1
    mascota1=0
    while cont<=M:
        cont1=0
        suma=0
        while cont1<N:
            mascotas=int(input("¿Cuantas mascotas habitan en el apartamento? "))
            if mascotas==1:
                mascota1+=1
            suma+=mascotas
            cont1+=1
        print("El conjuto ", cont, "tiene ", suma, "mascotas")
        cont+=1
    print(mascota1, "encuestados tienen una mascota")
def multiCalculadora():
    num=0
    acumulado=0
    bandera=True
    while num!=-1:
        num=int(input("Escriba un número: "))
        if bandera==True:
            menor=num
            bandera=False
        if num<menor and num!=-1:
            menor=num
        if acumulado==0:
            acumulado+=num
        else:
            if num%6==0:
                acumulado+=num
            elif num%9==0:
                acumulado*=num
            elif num%7==0:
                acumulado-=num
            elif num%5==0:
                acumulado/=num
    print("El acumulado es ", acumulado)
    print("El número más pequeño ingresado por el usuario es ", menor)
def vivaAir():
    def f_calculoBase(km, tiempo, modalidad):
        if modalidad=="alacarta":
            valorBase=(km/100)*45000
        elif modalidad=="combo+":
            valorBase=(km/70)*25000+(tiempo/30)*10000
        elif modalidad=="combo++":
            valorBase=(km/50)*25000+(tiempo/60)*1000
        return(valorBase)
    def f_costoAdicional(formaPago, modalidad, maletasBod, vuelo):
        if vuelo=="nacional":
            precio=70000
        elif vuelo=="internacional":
            precio=250000
        if modalidad=="alacarta":
            valorAdicional=maletasBod*precio
        elif modalidad=="combo+":
            valorAdicional=(maletasBod-1)*precio
        elif modalidad=="combo++":
            valorAdicional=(maletasBod-2)*precio
        if formaPago=="si":
            valorAdicional*=0.7
        return(valorAdicional)
    def p_calculoTiquete():
        nombre=input("Nombre: ")
        km=float(input("Kilómetros de viaje: "))
        tiempo=float(input("Minutos de vuelo: "))
        modalidad=input("Escriba la modalidad del vuelo (alacarta, combo+ o combo++, sin espacios y en minuscula) " )
        formaPago=input("¿El pago se realizó por internet? (Escriba si o no) ")
        maletasBod=int(input("Número de maletas que desea llevar por bodega: "))
        vuelo=input("¿El vuelo es nacional o internacional? ")
        valorBase=f_calculoBase(km, tiempo, modalidad)
        valorAdicional=f_costoAdicional(formaPago, modalidad, maletasBod, vuelo)
        valorFinal=valorBase+valorAdicional
        print(nombre)
        print("El valor que tendrá que pagar por su tiquete es de ", int(valorFinal))
    p_calculoTiquete()
sondeoHospitalMascotas()
multiCalculadora()
vivaAir()






















    
            
