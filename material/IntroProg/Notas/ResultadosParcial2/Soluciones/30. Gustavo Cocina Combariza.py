def punto1()
    conjuntos=int(input("¿CUANTOS CONJUNTOS RESIDENCIALES HAY?"))
    cont=0
    aptospar=0
    while cont1<conjuntos:
        apartamentos=int(input(cont1,": ¿CUÁNTOS APARTAMENTOS TIENE ESTE CONJUNTO?"))
        suma=0
        while cont2<apartamentos:
            mascotas=int(input(cont2,": ¿CUÁNTAS MASCOTAS RESIDEN EN ESTE APARTAMENTO?"))
            suma+=mascotas
            if mascotas==2:
            aptospar+=1
        print(suma,":CANTIDAD DE MASCOTAS POR CONJUNTO RESIDENCIAL")
    print(aptospar,": ESTE ES EL NUMERO DE APTOS QUE TIENEN 2 MASCOTAS")


    def calculoBase(modalidad,distancia,minutos)
    if modalidad==1
        preciotiquete=(55000*(distancia//100))
    elif modalidad==2
        preciotiquete=(25000*(distancia//70))+(10000*(minutos//30))
    elif modalidad==3
        preciotiquete=(25000*(distancia//50))+(10000*(minutos//60))
    return preciotiquete

    def costoAdicional(modalidad,tipodepago,cantmaletas,tipodevuelo)
    if modalidad==1:
        if cantmaletas>0:
            if tipodevuelo==1:
                costoad=cantmaletas*70000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
            else:
                costoad=cantmaletas*250000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
            
    elif modalidad==2:
        if cantmaletas>1:
            if tipodevuelo==1:
                costoad=cantmaletas*70000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
            else:
                costoad=cantmaletas*250000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
                
    elif modalidad==3
        if cantmaletas>2
            if tipodevuelo==1
                costoad=cantmaletas*70000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
            else:
                costoad=cantmaletas*250000
                if tipodepgao==1:
                    costoad=(costoad*.7)
                    print(costoad)
                else:
                    print(costoad)
    return costoad

    nombre:int(input("INGRESE SU NOMBRE"))
    print("MODALIDAD OPCIÓN1. A LA CARTA")
    print("OPCIÓN2. COMBO+")
    print("OPCIÓN3. COMBO++")
    modalidad=int(input("SELECCIONE EL NUMERO DE LA OPCION QUE DESEE"))   
    distancia=int(input("INGRESE LA DISDTANCIA EN KM´S DE RECORRIDO"))
    minutos=int(input("INGRESE EL TIEMPO EN MINUTOS QUE SE DEMORARA EL VUELO")
    print("TIPO DE PAGO. OPCION1. VIA INTERNET")
    print("OPCION2. PRESENCIAL")
    tipodepago=int(input("SELECCIONE EL TIOPO DE PAGO 1 ó 2"))
    cantmaletas=int(input("INGRESE LA CANTIDAD DE MALETAS DE BODEGA EXTRA"))
    tipodevuelo=int(input("TIPO DE VUELO.  1. NACIONAL  2. INTERNACIONAL"))
    cotototal=(calculoBase(modalidad,distancia,minutos)+costoAdicional(modalidad,tipodepago,cantmaletas,tipodevuelo))
    cototal=costoad+preciotiquete
    print(cototal," PRECIO TOTAL DEL TIQUETE")

def punto3()
    cont=0
    acu=0
    suma=0
    bandera=True
    while cont!=-1:
        calculadora=int(input("INGRESE UN VALOR"))
        menor=calculadora
        cont=calculadora
        if calculadora!=-1:
            acu+=calculadora  # malo
            if calculadora%8==0:
                acu+=calculadora
            elif calculadora%9==0:
                acu=acu*calculadora
            elif calculadora%7==0:
                acu=acu-calculadora
            elif calculadora%5==0:
                acu=acu//calculadora
            if menor>calculadora:
                bandera=False
            if bandera==False:
                print(calculadora,":  ESTE ES EL MENOR")
            if calculadora==0:
                acu=0
                print(acu,":  ESTE ES EL ACUMULADO")
            suma+=acu
            print(suma,":  ESTE ES EL ACUMULADO")
        if menor==calculadora:
            bandera=False
        if bandera==False:
            print(calculadora,":  ESTE ES EL MENOR")
        else:
            print(acu,"ESTE ES EL ACUMULADO")

respuesta=int(input("QUE PREGUNTA DESEA RESPONDER. 1, 2 Ó 2")
    if respuesta==1:
        respuesta=punto1()
        print(respuesta)
    elif respuesta==2:
        respuesta=punto2()
        print(respuesta)
    elif:
        respuesta=punto3
        print(respuesta)
              
        
    
    



    
    
