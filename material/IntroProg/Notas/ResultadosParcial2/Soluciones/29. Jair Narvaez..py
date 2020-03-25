
def ejercicio1(ejer):
    n = int(input("Diga la cantidad de conjuntos residenciales: "))
    m = int(input("\nDiga la cantidad de apartamentos del conjunto: "))
    cont_n = 1
    suma_mascot = 0
    mascota0 = 0
    while cont_n <= n:
        print(f"\nConjunto {cont_n}\n")
        cont_m = 1
        suma_mascot = 0
        while cont_m <= m:
            mascotas = int(input(f"Apartamento {cont_m}: "))
            if mascotas == 0:
                mascota0 += 1
            suma_mascot += mascotas
            cont_m += 1
        print(f"\nEn total hay {suma_mascot} mascotas en el conjunto {cont_n}")
        cont_n += 1
    print(f"\nHay 0 mascotas en {mascota0} apartamentos")



def ejercicio2(ejer):
    def multi(num):
        compar = 0
        acumulado = 0
        m = True
        
        while (num != -1):
            num = int(input("Diga un numero: "))
            if m == True:
                compar = num * 1000  # Est multiplicacio nno es necesaria
                m = False
            if acumulado == 0:
                acumulado += num
            if num % 4 == 0:
                acumulado += num
            elif num % 9 == 0:
                acumulado *= num
            elif num % 7 == 0:
                acumulado -= num
            elif num % 5 == 0:
                acumulado /= num
            print(acumulado)

            if compar <= num:
                compar = num
        print(f"El menor es {compar} ")
        return acumulado

    num = 0
    acumulado = multi(num)




def ejercicio3 (ejer):

    def f_calculoBase(distancia, tiempo, modalidad):
        if modalidad == 1:
            valor_base = (distancia / 100)
        elif modalidad == 2:
            valor_base = (distancia / 70) * 25000 + (tiempo / 30) * 10000
        elif modalidad == 3:
            valor_base = (distancia / 50) * 25000 + (tiempo / 60) * 10000
        return valor_base

    def f_costoadicional(maleta):
            
            maleta = int(input("Diga la cantidad de maletas: "))
            if modalidad == 2:
                maleta = maleta - 1
            print("\n¿Descuento por internet?\n")
            descuento = int(input("1.Si\n2.No\n"))
            if descuento == 1:
                descuento = 0.3
            else:
                descuento = 0

            valor_adicional = (1 - descuento) *(maleta * 70000)
            return valor_adicional

    def p_calculotiquete (valor_base,valor_adicional):
        valor_total= valor_base +valor_adicional
        return valor_total

    print(f"1. A la carta\n2. Combo +\n3.Combo ++")
    modalidad = int(input("\nEscoja la modalidad: "))
    
    distancia = int(input("Diga la distancia del vuelo: "))
    tiempo = int(input("Diga el tiempo del vuelo: "))

    valor_base = f_calculoBase(distancia, tiempo, modalidad)

    print("\n¿Desea servicios adicionales?\n")
    adicional = int(input("1.Si\n2.No\n"))
    if adicional == 1:
        maleta =  0
        valor_adicional = f_costoadicional(maleta)

    valor_total = p_calculotiquete(valor_base,valor_adicional)
    print(f"El valor final es: {valor_total}")


print(f"1.Ejercicio1\n2.Ejercicio2\n3.Ejercicio3\n")
ejer = int(input("Diga el ejercicio: " ))
if ejer == 1:
    ejercicio1(1)
if ejer == 2:
    ejercicio2(1)
if ejer == 3:
    ejercicio3(1)
