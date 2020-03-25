#eduardo avendaño

def ejercicio1():
    conjuntos=int(input("ingrese el numero de conjuntos: "))
    contconjuntos=0
    apartamentos=0
    mascotas3=0

    while contconjuntos<conjuntos:
        contconjuntos+=1
        contapartamentos = 0
        sumaMascotas = 0
        print("conjunto",contconjuntos,":")
        apartamentos=int(input("ingrese la cantidad de apartamentos que tiene su conjunto: "))
        while contapartamentos<apartamentos:
            contapartamentos+=1
            print("apartamento",contapartamentos,":")
            numMascotas=int(input("cuantas mascotas tiene su apartamento: "))


            if numMascotas>=3:
                mascotas3+=1
            sumaMascotas=sumaMascotas+numMascotas
        print("el numero de mascotas en el conjunto",contconjuntos,"es de:",sumaMascotas)
    print("la cantidad de apartamentos que poseen 3 o mas mascotas es:",mascotas3)




def ejercicio2():
    acumulado=0
    entrante=0
    primera=0
    menor=0
    contmenor=0

    while entrante!=-1:
        entrante=int(input("ingrese un numero entero o pulse -1 para salir del programa "))
        primera+=1
        contmenor+=1
        if contmenor==1 and entrante!=-1:
            menor=entrante
        if primera==1 and entrante!=-1:
            acumulado=entrante
        elif entrante%12==0:
            acumulado=acumulado+entrante
        elif entrante%9==0:
            acumulado=acumulado*entrante
        elif entrante%7==0:
            acumulado=acumulado-entrante
        elif entrante%5==0:
            acumulado=acumulado/entrante
        else:
            acumulado=acumulado
        if entrante<menor and entrante!=-1:
            menor=entrante
    print("el acumulado final es de:",acumulado)
    print("el numero menor fue:",menor)




def ejercicio3():
    def f_calculoBase(distancia,minutos,plan):
        costo=0
        if plan==1:
            costo=distancia/100*65000
        if plan==2:
            costo=(distancia/70)*25000+(minutos/30)*10000
        if plan==3:
            costo=(distancia/50)*25000+(minutos/60)*10000
        return costo
    def f_costoAdicional(pago,plan,maletas,vuelo):
        adicional=0
        if plan==1:
            maletas=maletas
            if pago==1:
                if vuelo==1:
                    adicional=0.7*(maletas*70000)
                if vuelo==2:
                    adicional=0.7*(maletas*250000)
            if pago==2:
                if vuelo==1:
                    adicional=(maletas*70000)
                if vuelo==2:
                    adicional=(maletas*250000)
        if plan==2:
            maletas=maletas-1
            if pago==1:
                if vuelo==1:
                    adicional=0.7*(maletas*70000)
                if vuelo==2:
                    adicional=0.7*(maletas*250000)
            if pago==2:
                if vuelo==1:
                    adicional=(maletas*70000)
                if vuelo==2:
                    adicional=(maletas*250000)
        if plan==3:
            maletas=maletas-2
            if pago==1:
                if vuelo==1:
                    adicional=0.7*(maletas*70000)
                if vuelo==2:
                    adicional=0.7*(maletas*250000)
            if pago==2:
                if vuelo==1:
                    adicional=(maletas*70000)
                if vuelo==2:
                    adicional=(maletas*250000)
        return adicional


    def f_calculoTiquete():
        nombre=input("ingrese su nombre ")
        pago=int(input("ingrese el tipo de pago que desea hacer, internet=1 o fisico=2 "))
        distancia=float(input("ingrese la distancia de su vuelo: "))
        plan=int(input("ingrese que tipo de plan compro, a la carta=1, combo+=2 y combo++=3 "))
        minutos=int(input("ingrese el tiempo de su vuelo en minutos: "))
        maletas=int(input("cuantas maletas adicionales desea llevar en la bodega: "))
        vuelo=int(input("indique si su vuelo es: nacional=1 o internacional=2 "))
        costo=f_calculoBase(distancia,minutos,plan)
        adicional=f_costoAdicional(pago,plan,maletas,vuelo)
        costoTotal=costo+adicional
        print("señor/a",nombre,"el costo total de su viaje es de:",costoTotal)

    f_calculoTiquete()

print("ejercicio 1")
ejercicio1()
print("ejercicio 2")
ejercicio2()
print("ejercicio 3")
ejercicio3()




























