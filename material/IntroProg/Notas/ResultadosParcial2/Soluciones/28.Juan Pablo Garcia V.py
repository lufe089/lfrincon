#Juan Pablo Garcia Vicuña
def ejercicio1():
 conjuntos=int(input("ingrrese el # de conjuntos residenciales"))
 conj=1
 suma11=0
 while conj<=conjuntos :
     aptos=int(input("ingrese el # de apartamentos "))
     cona=0
     suma1=0
     sumaMascotas=0
     while cona<aptos:
         mascotas=int(input("¿cuantas mascotas tiene?"))
         if mascotas==1:
           suma1+=1
         sumaMascotas+=mascotas
         cona+=1
     if cona==aptos:
         print("el conjunto tiene ", suma1, "apartamentos con una sola mascota")
         print("El conjunto tine ", sumaMascotas ,"mascotas en total")
     conj+=1
     suma11+=suma1
 print("En total hay ", suma11," apartamentos con 1 mascota")
 PUNTO1=ejercicio1()
 print(PUNTO1)
def ejercicio2():#no funciona
    NEntrante = int(input("ingrese un numero ")) # error
    while NEntrante != -1:
     acumulado=0  # error
     if NEntrante/6==0:
        acumulado+=NEntrante
        print(acumulado)
     elif NEntrante/9==0:
        acumulado=NEntrante*acumulado
        print(acumulado)
     elif NEntrante%7==0:
        acumuluado=NEntrante-acumulado
     elif NEntrante%5==0:
        acumulado=acumulado/NEntrante
        print(acumulado)
ejer=ejercicio2()
print(ejer)
def f_calculobase():
    distancia=float(input("ingrese la distancia en KM del vuelo : "))
    tiempo=float(input("ingrese el tiempo de vulo en min : "))
    modalidad=int(input("INGRESE # A LA CARTA (1) , COMBO+(2), COMBO++(3)"))
    if modalidad==1:
        print("El valor base de su vuelo es : ",(distancia/100)*45000)

    elif modalidad==2:
        print("El valor base de su vuelo es : ",((distancia/70)*25000)+(tiempo/30)*1000)

    elif modalidad==3:
        print("El valor base de su vuelo es : ",((distancia/50)*25000)+(tiempo/60)*1000)
costo=f_calculobase
print(costo)

def f_costoAdicional:
    Fpago=int(input("PARA SU FORMA DE PAGO INGRESE(1) INTERNET (2)NORMAL"))
    modalidad = int(input("INGRESE # A LA CARTA (1) , COMBO+(2), COMBO++(3)"))
    maletas=int(input("ingrese la cantidad de maletas"))
    tipo=int(input"ingre")

    if Fpago==1 and modalidad==1 and  :
        if maletas<1
            print("debe pagar adicional", 0.7)











