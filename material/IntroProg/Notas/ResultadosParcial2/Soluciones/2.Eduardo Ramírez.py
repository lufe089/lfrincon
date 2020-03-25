#Eduardo José Ramírez

#mascotas
def mascotas():
    conjuntos=int(input("Número de conjuntos: "))
    apartamentos=int(input("Número de apartamanetos por conjunto: "))
    cont1=0
    contadorcero=0
    cont=1
    while cont1<conjuntos:
        cont2=0
        contmascotas=0
        print("Conjunto",cont)
        while cont2<apartamentos:
            mascotas=int(input("Número de mascotas: "))
            if mascotas==0:
                 contadorcero+=1
            else:
                contmascotas+=mascotas
            cont2+=1
        print("El número de mascotas de este conjunto son: ",contmascotas)
        cont1+=1
        cont+=1
    print("De los apartamentos , no tienen mascotas: ",contadorcero)
       
#multicalculadora
def Multicalculadora():
    num=0
    acumulado=0
    bandera=0
    while num!=-1:
        num=int(input("Número: "))
        if num!=-1:
            if acumulado==0:
                acumulado+=num
            elif num%4==0:
                acumulado+=num
            elif num%9==0:
                acumulado*=num
            elif num%7==0:
                acumulado-=num
            elif num%5==0:
                acumulado/=num
            else:
                acumulado+=0
            if bandera==0:
                menor=num
                bandera=1
            elif num<menor:
                menor=num
    print("El acumulado es: ",acumulado)
    print("El menor número ingresado (sin contar -1) es: ",menor)
    

#aereolinea

def fCalculoBase(distancia,minutos,tiq):
    if tiq=="a la carta":
        vbase=(distancia/100)*35000
    elif tiq=="Combo+":
        vbase=(distancia/70)*25000+(minutos/30)*10000
    elif tiq=="Combo++":
        vbase=(distancia/50)*25000+(minutos/60)*10000
    return vbase
def fCalculoAdicional(pago,tiq,maletas,vuelo):
    vadicional=0
    if tiq=="a la carta" and maletas>0:
        maletas+=0
        if vuelo=="nacional":
            vadicional+=(70000*maletas)
        else:
            vadicional+=(250000*maletas)
    elif tiq=="Combo+" and maletas>1:
        maletas=maletas-1
        if vuelo=="nacional":
            vadicional+=(70000*maletas)
        else:
            vadicional+=(250000*maletas)
    elif tiq=="Combo++" and maletas>2:
        maletas=maletas-2
        if vuelo=="nacional":
            vadicional+=(70000*maletas)
        else:
            vadicional+=(250000*maletas)
    if pago=="internet":
        vadicional*=0.7
    else:
        vadicional+=0
    return vadicional

def CalculoTiquete():
    nombre=input("Nombre de usuario: ")
    tiq=input("Modalidad tiquete (a la carta,Combo+,Combo++): ")
    vuelo=input("Vuelo nacional o internacional: ")
    distancia=int(input("Distancia en kilometros del viaje: "))
    minutos=int(input("Tiempo en minutos del viaje: "))
    pago=input("Pago realizado por internet o normal: ")
    maletas=int(input("Número de maletas en bodega: "))
    valorbase=fCalculoBase(distancia,minutos,tiq)
    valoradicional=fCalculoAdicional(pago,tiq,maletas,vuelo)
    print(nombre,", debes pagar por tu tiquete: ",valorbase+valoradicional)

mascotas()
Multicalculadora()
llamado3=CalculoTiquete()

    


        

    

    
