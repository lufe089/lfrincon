##Juan Manuel Arias Gallego
def ejercicio3():
    def calculoBase(distancia, tiempoVuelo, modalidad):
        precio = 0
        divisorkilometros=0
        tiempoDivisor=0
        costoTiempo=0
        if modalidad==1:
            precio=55000
            divisorkilometros= 100
            tiempoDivisor=1
            costoTiempo=1
        if modalidad==2:
            precio=25000
            divisorkilometros= 70
            tiempoDivisor= 30
            costoTiempo= 10000
        if modalidad==3:
            precio=25000
            divisorkilometros= 50
            tiempoDivisor= 60
            costoTiempo=10000

        valorBase=(distancia/divisorkilometros)* precio + (tiempoVuelo/tiempoDivisor) * costoTiempo

        return valorBase

    def calculoAdicional (internet, maletas, tipoVuelo, modalidad ):
        valorAdicional=0
        valorMaletas=0
        numPermitidoMaletas=0
        if modalidad==1:
            numPermitidoMaletas=0
        elif modalidad==2:
            numPermitidoMaletas=1
        elif modalidad==3:
            numPermitidoMaletas=2

        if internet==1 and tipoVuelo==1:
            valorAdicional= 0.7*((maletas-numPermitidoMaletas)*70000)
        elif internet==2 and tipoVuelo==1:
            valorAdicional= ((maletas-numPermitidoMaletas)*70000)
        elif internet==1 and tipoVuelo==2:
            valorAdicional = ((maletas-numPermitidoMaletas) * 250000)
        elif internet == 2 and tipoVuelo == 2:
            valorAdicional = ((maletas-numPermitidoMaletas) * 250000)

        return valorAdicional


    def valorFinal(x,y):
        cuentaTotal= x + y
        return cuentaTotal

    nombre=str(input("Digite su nombre "))
    modalidad=int(input("Digite 1 si su modalidad es A la carta.     Digite 2 si su modalidad es Combo+.     Digite 3 si su modalidad es Combo++ "  ))
    tipoVuelo=int(input("Digite 1 si su vuelo es nacional.     Digite 2 si su vuelo es internacional" ))
    tiempoVuelo=int(input("Ingrese el tiempo que demora el vuelo "))
    distancia=int(input("Ingrese la distancia del viaje en kilómetros "))
    internet=int(input(" Digite 1 si la compra fue realizada por internet.     Digite 2 si la compra NO fue realizada por internet "))
    maletas=int(input("Digite la cantidad de maletas que desea llevar "))
    calculoBase(distancia, tiempoVuelo, modalidad)
    calculoAdicional(internet, maletas, tipoVuelo, modalidad)
    y=calculoBase(distancia, tiempoVuelo, modalidad)
    x=calculoAdicional(internet, maletas, tipoVuelo, modalidad)
    z=valorFinal(x, y)
    print(nombre, "El valor base del tiquete es: ", (calculoBase(distancia, tiempoVuelo, modalidad)))
    print(nombre, "El valor adicional es: ", x)
    print(nombre, "El valor total es: ", z)

def ejercicio2():
    cont=0
    cantidadNumeros=int(input("Digite la cantidad de números que vas a calcular "))

    while cantidadNumeros>= cont:
        acumulado=0 # no sirve para nada
        num=int(input("Ingrese el número a operar "))

        if num%8==0:
            num+=acumulado
            print(num, ",", acumulado)
        if num%9==0:
            num=num*acumulado
            print(num, ",", acumulado)
        if num%7==0:
            num= num-acumulado
            print(num, ",", acumulado)
        if num%5==0:
            num= num/acumulado
            print(num, ",", acumulado)
        if num==-1:
            break
        else:
            print("0 ",num )
        acumulado=num
        cont+=1


ejercicio3()
ejercicio2()