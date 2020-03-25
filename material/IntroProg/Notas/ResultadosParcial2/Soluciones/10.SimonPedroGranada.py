def ejercicio1():
    conjunto=int(input("ingrese el numero de conjuntos residenciales"))
    apto=int(input("ingrese el numero de apartamentos"))
    contApto=0
    contConjunto=0
    aptosCon2Mascotas=0
    mascotasConjunto=0
    while contConjunto<conjunto:

        while contApto< apto:
            mascostas=int(input("cuantas mascotas tienen el su apartamento?"))
            mascotasConjunto+=mascostas
            contApto+=1
            if mascostas==2:
                aptosCon2Mascotas+=1
        contConjunto+=1
        print("el conjunto", contConjunto,"tiene", mascotasConjunto, "mascotas")
        mascotasConjunto=0
        contApto=0
    print("los apartamentos que tienen 2 mascostas son", aptosCon2Mascotas)

def ejercicio2():
    acumulado = 0
    numeroEntrante = 0
    menor = 2000000000000000
    while numeroEntrante != -1:
        numeroEntrante = int(input("ingrese un numero"))
        if acumulado == 0:
            acumulado += numeroEntrante
        elif numeroEntrante % 8 == 0:
            acumulado += numeroEntrante

        elif numeroEntrante % 9 == 0:
            acumulado *= numeroEntrante

        elif numeroEntrante % 7 == 0:
            acumulado -= numeroEntrante

        elif numeroEntrante % 5 == 0:
            acumulado = acumulado / numeroEntrante

        if numeroEntrante < menor and numeroEntrante != -1:
            menor = numeroEntrante

    print("el acumulado es", acumulado)
    print("el numero menor es:", menor)

def ejercicio3():
    def p_calculoTiquete():
        nombre = input("ingrese su nombre")
        modalidad = int(
            input("escriba 1 para modalidad: A la carta, 2 para modalidad: Combo + , 3 para la modalidad: Combo ++ "))
        vuelo = int(input("ingrese 1 para vuelos Nacionales, o 2 para vuelos internacionales"))
        maletasAdicionales = int(
            input("ingrese el numero de maletas adicionales que quiere llevar, si no lleva ninguna escriba 0"))
        distancia = int(input("ingrese la distancia en km que hay hasta su destino"))
        tiempo = int(input("ingrese el tiempo en minutos de su vuelo"))
        formaPago = int(input("ingrese 1 para pago por internet o 2 para pago normal"))

        costoBase = f_calculoBase(distancia, tiempo, modalidad)
        costoAdicional = f_costoAdicional(formaPago, modalidad, maletasAdicionales, vuelo)
        totalPagar = costoBase + costoAdicional
        print(nombre, totalPagar)

    def f_calculoBase(distancia, tiempo, modalidad):
        valor_base = 0
        if modalidad == 1:
            valor_base = (distancia / 100) * 55000
        elif modalidad == 2:
            valor_base = (distancia / 70) * 25000 + (tiempo / 30) * 10000
        elif modalidad == 3:
            valor_base = (distancia / 50) * 25000 + (tiempo / 60) * 10000
        return valor_base

    def f_costoAdicional(formaPago, modalidad, maletasAdicionales, vuelo):
        if modalidad == 2:
            maletasAdicionales -= 1
        elif modalidad == 3:
            maletasAdicionales -= 2
        if vuelo == 1:
            valorAdicional = maletasAdicionales * 70000
        elif vuelo == 2:
            valorAdicional = maletasAdicionales * 250000
        if formaPago == 1:
            valorAdicional *= 0.7
        return valorAdicional

    p_calculoTiquete()

ejercicio1()
ejercicio2()
ejercicio3()



