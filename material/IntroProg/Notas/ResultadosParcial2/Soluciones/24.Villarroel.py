#Juan Esteban Villarroel
def encuesta():
    cont1=1
    totalMascotas1 =0
    ceroMascotas=0
    conjunto=int(input("cuantos conjuntos quiere encuestar?: "))
    while cont1<=conjunto:
        apto=int(input("cuántos aptos tiene el conjunto: "))
        cont2=1
        while cont2<=apto:
            mascotas=int(input("cuántas mascotas tiene el apartamento?: "))
            if mascotas==0:
                ceroMascotas +=1
            totalMascotas1 +=mascotas
            print("EL APARTAMENTO ",cont2," TIENE ",mascotas," MASCOTAS")
            cont2 +=1
        cont1 +=1
    print("APARTAMENTOS SIN MASCOTAS: ",ceroMascotas)
encuesta()



def calculadora():
    ac=0
    totalAc=0
    menor=9**9
    while ac!=-1:
        ac=int(input("ingrese un valor(para el acumulado): "))
        if ac<menor:
            menor=ac
        if ac==0:
            totalAc=ac
        else:
            if ac%4==0:
                totalAc +=ac
            elif ac%9==0:
                totalAc *=ac
            elif ac%7==0:
                totalAc -=ac
            elif ac%5==0:
                totalAc =totalAc/ac
            else:
                totalAc==ac
        print("el acumulado de la calculadora es: ",totalAc)
        print("el menor de los números ingresados es ",menor)
calculadora()

def f_calculoBase(modalidad):
    valor_base=0
    km=int(input("cuantos km tiene el recorrido?: "))
    minutos=int(input("cuántos minutos dura el viaje?: "))
    if modalidad==1: #a la carta
        valor_base=((km/10)*35000)
    elif modalidad==2: #combo+
        valor_base=(((km/70)*25000)+((minutos/30)*10000))
    elif modalidad==3: #combo++
        valor_base==(((km/50)*25000)+((minutos/60)*10000))
    return valor_base
print("elija una modalidad: (DIGITE NÚMERO) \n1. a la carta\n2. Combo+\n3. Combo++")
modalidad=int(input())
valor=f_calculoBase(modalidad)
print("el valor del tiquete es ",int(valor))

def f_costoAdicional(formaPago,modalidad,maletas,vuelo):
    valorMaletas=0
    if modalidad==1:
        print("no puede llevar maletas en bodega")
    else:
        if vuelo==1
            if modalidad==2:
                if maletas<=1:
                    valorMaletas=0
                else:
                    valorMaletas=(maletas-1)*70000
            if modalidad==3:
                if maletas<=2:
                    valor maletas=0
                else:
                    valorMaletas=(maletas-2)*70000
        if vuelo==2:
            if modalidad==2:
                if maletas<=1:
                    valorMaletas=0
                else:
                    valorMaletas=(maletas-1)*250000
            if modalidad==3:
                if maletas<=2:
                    valor maletas=0
                else:
                    valorMaletas=(maletas-2)*250000
            
    return valorMaletas
            
print("forma de pago (ingrese número)\n1. normal\n2. internet"))
formaPago=int(input())
print("elija una modalidad: (DIGITE NÚMERO) \n1. a la carta\n2. Combo+\n3. Combo++")
modalidad=int(input())
maletas=int(input("cuántas maletas desea llevar por bodega?: "))
print("cómo es su vuelo? (ingrese número):\n1.nacional\n2.internacional")
vuelo=int(input())
valor_a=f_costoAdicional(formaPago,modalidad,maletas,vuelo)
print("el costo adicional es: ",valor_a)




