#Funciones y procedimientos
def f_calculoBase (dist, minu, mod):
    valbase= 0
    if mod == "a":
        valbase= (dist/100)*65000
    elif mod == "b":
        valbase= (dist/70)*25000+(minu/30)*10000
    elif mod == "c":
        valbase= (dist/50)*25000+(minu/60)*10000
    return valbase



def f_costoAdicional (forp, mod, cantm, tipv):
    valad= 0
    if mod == "a" and cantm >= 1:
        if tipv == "N":
            valad= cantm*70000
        elif tipv == "I":
            valad= cantm*250000
    elif mod == "b" or mod == "c" and cantm > 1:
        if tipv == "N":
            valad= cantm*70000
        elif tipv == "I":
            valad= cantm*250000
    if forp == "si":
        valad=valad*0.7
    if forp == "no":
        valad=valad
    return valad



def p_calculoTiquete (nom):
    dist=float(input("Ingrese la distancia del vuelo en kilometros: "))
    minu=int(input("Ingrese el tiempo del vuelo en minutos: "))
    mod=input(str("Ingrese la modalidad \n(A la carta = a, Combo+ = b, Combo++ = c): "))
    if mod == "a" or mod == "b" or mod == "c":
        cantm=int(input("Ingrese la cantidad de maletas a llevar en bodega: "))
        tipv=input("¿El vuelo es Nacional o Internacional? \n Responda N o I respectivamente: ")
        if tipv == "N" or tipv == "I":
            forp=input("¿Paga por internet? \n Responda si/no: ")
            if forp =="si" or forp =="no":
                valti=(f_calculoBase (dist, minu, mod))+(f_costoAdicional (forp, mod, cantm, tipv))
                print(nom, "el valor de su tiquete es de ", valti, "pesos")
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")


def multicalculadora (acum):
    cont=0
    menor=1000000000000000000000000000000000000000000000000000000000000000000000000000
    while cont !=-1:
        num=int(input("Ingrese un número entero: "))
        cont=num
        if acum == 0:
            acum+=num
        elif acum !=0:
            if num%12==0:
                acum+=num
            elif num%9==0:
                acum*=num
            elif num%7==0:
                acum-=num
            elif num%5==0:
                acum/=num
            elif num == -1:
                cont=num
        if num < menor:
            if num == -1:
                menor=menor
            else:
                menor=num        
        print(acum)
    print("El número más pequeño ingresado fue ", menor)

def SondeoMasc(conj,apt):
    cont=1
    mumas=0
    while cont <= conj:
        cont1=1
        tmas= 0
        while cont1 <= apt:
            print("Conjunto ", cont, " apartamento ", cont1)
            mas=int(input("Ingrese el número de mascotas del apartamento: "))
            cont1+=1
            tmas+=mas
            if mas >= 3:
                mumas+=1
        print("El conjunto ", cont, " tiene un total de ", tmas, " mascotas.")
        cont+=1
    print("Hay un total de ", mumas, " apartamentos con más de 3 mascotas.")

    

#Llamados
conj=int(input("Ingrese el número de conjuntos: "))
apt=int(input("Número de apartamentos a encuestar por conjunto: "))
enc=SondeoMasc(conj,apt)



acum=int(input("Ingrese el número en el cual quiere que empiece el acumulador \n Preferiblemente 0: "))
cal=multicalculadora(acum)



nom=input("Ingrese su nombre o el de la persona que va a viajar: ")
tik= p_calculoTiquete(nom)



    
    
