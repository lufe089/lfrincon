#Nel Krauss Tovar

def primero ():
    conjuntos=int(input("Ingrese numero de conjuntos: "))
    cont1 = 1
    sumaPetsTotal=0
    aptoMascota=0
    while cont1<=conjuntos:
        cont = 1
        sumaPets=0
        apartamentos = int(input("Ingrese numero de apartamentos: "))
        while cont<=apartamentos:
            pets=int(input("ingrese cuantas mascotas tiene:"))
            if pets>0:
                aptoMascota+=1
            sumaPetsTotal+=pets
            sumaPets+=pets
            cont+=1
        print (cont1,"conjunto tiene: ",sumaPets, "mascotas")
        cont1+=1
    print("Total de apartamentos con mascota: ",aptoMascota)

def segundo ():
    num=0
    acumulado=0
    menor=0
    bandera=True
    while num != -1:
        num = int(input("ingrese un numero"))
        if num!=-1:
            if bandera==True:
                menor=num
                bandera=False
            if num%6==0:
                acumulado+=num
            elif num%9==0:
                acumulado*=num
            elif num%7==0:
                acumulado-=num
            elif num%5==0:
                acumulado/=num
            else:
                acumulado=acumulado
        if acumulado==0:
            acumulado=num
        if num<menor and num!=-1:
            menor=num
    print("el acumulado es: ",acumulado)
    print("el menor numero ingresado es:",menor)

def tercero():

    def f_calculoBase(distancia,tiempo,plan):
        valorBase=0
        if plan==1:
            valorBase=45000*(distancia/100)
        elif plan==2:
            valorBase=(25000*(distancia/70))+(10000*(tiempo/30))
        elif plan==3:
            valorBase = (25000 * (distancia / 50)) + (10000 * (tiempo / 60))
        return valorBase

    def f_costoAdicional(fpago,plan,maletas,vuelo):
        costomaleta=0
        if plan==1 and maletas>0:
            if vuelo:
                costomaleta=maletas*70000
            else:
                costomaleta=maletas*250000
        elif plan==2 and maletas>1:
            if vuelo:
                costomaleta=(maletas-1)*70000
            else:
                costomaleta=(maletas-1)*250000
        elif plan==3 and maletas>2:
            if vuelo:
                costomaleta=(maletas-2)*70000
            else:
                costomaleta=(maletas-2)*250000
        if fpago:
            costomaleta=costomaleta*0.7
        return costomaleta

    def p_calculoTiquete ():
        nombre=input("Escriba su nombre: ")
        plan = int(input("¿Que plan desea tomar?: 1=a la carta, 2=Combo+, 3=Combo++: "))
        tiempo = int(input("¿Cuanto dura su vuelo en minutos?: "))
        distancia = float(input("¿De cuantos Km es su vuelo?: "))
        fpago=int(input("Forma de pago: 1-Internet, 2-Normal"))
        maletas=int(input("Numero de maletas que lleva: "))
        vuelo=int(input("Tipo de vuelo: 1-Nacional, 2-Internacional"))
        if fpago==1:
            fpago=True
        else:
            fpago=False
        if vuelo==1:
            vuelo=True
        else:
            vuelo=False
        calculoBase=f_calculoBase(distancia,tiempo,plan)
        calculoAdicional=f_costoAdicional(fpago,plan,maletas,vuelo)
        costoTotal=calculoBase+calculoAdicional

        print(nombre)
        print("Valor final a pagar: ", int(costoTotal))

    p_calculoTiquete()

primero()
segundo()
tercero()






