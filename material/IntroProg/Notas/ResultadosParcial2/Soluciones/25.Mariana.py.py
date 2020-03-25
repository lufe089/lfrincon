#sondeo de mascotas
conjuntos=int(input("A cuántos conjuntos residenciales va a hacer la encuesta? "))
conj=0
while conjuntos>conj:
    n_apto=1
    n_Mascotas=0
    cero_Masco=0
    apto=int(input("¿cuantos apartamentos son? "))
    if apto>n_apto:
        n_Mascotas = 0
        apto2=int(input("Cuantas mascotas tiene?"))
        if apto2>=1:
            n_Mascotas+=apto2
        else:
            if apto2==0:
                cero_Masco+=1
    n_apto+=1
    print(n_Mascotas)
    print(cero_Masco)


def Mascotas():
    MascotaApto = int(input("Cuantas mascotas tiene?: "))
    contMascot = 0
    cont = 0
    cont1 = 0
    while MascotaApto > cont:
        if MascotaApto > cont:
            cont += contMascot

        else:
            if MascotaApto == 0:
                cont += 1
        cont1 += 1
        return Mascotas

    num = int(input("el # de numeros que va a ingresar: "))
    cont = 0
    while num >= cont:
        totalNum = 0
        acomulado = 0
        numero1 = int(input("ingrese el numero: "))
        if numero1 % 4 == 0:
            acomulado = acomulado + numero1
        elif numero1 % 9 == 0:
            acomulado = acomulado * numero1
        elif numero1 % 7 == 0:
            acomulado = numero1 - acomulado
        elif numero1 % 5 == 0:
            acomulado = acomulado / numero1
        elif num == -1:
            break
        else:
            acomulado = num
        totalNum += 1
        print(acomulado)

