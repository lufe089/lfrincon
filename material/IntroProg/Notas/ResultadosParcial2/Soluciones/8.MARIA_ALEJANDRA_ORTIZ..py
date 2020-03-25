#Maria Alejandra Ortiz
#ejercio1

def hospital(conjuntos):
    contConjuntos=1
    mascotasPorConjunto=0
    
    while contConjuntos<=conjuntos:
        print("Conjunto", contConjuntos)
        apartamentos=int(input("¿Cuántos apartamentos hay en el conjunto? "))
        
        contApartamentos=1
        unaMascota=0
        totalMascotas=0
        
        while contApartamentos<=apartamentos:
            print ("Apartamento", contApartamentos)
            mascotas=int(input("¿Cuántas mascotas hay en el apartamento? "))

            if mascotas==1:
                unaMascota+=1
                
                contApartamentos+=1
            else:
                contApartamentos+=1

            totalMascotas=totalMascotas+mascotas
                      
        print("El conjunto", contConjuntos, "tiene", totalMascotas, "mascotas")
        print("La cantidad de apartamentos que poseen una sola mascota son:", unaMascota)
        contConjuntos+=1

    

conjuntos=int(input("¿Cuántos conjuntos son? "))
hospital(conjuntos)
    
#ejercicio2

num=0
acumulado=0
while num!=-1:
    num=int(input("Ingrese un número: "))

    if acumulado==0:
        num=acumulado+num
        acumulado=num
        print(acumulado)
    else:
        while num!=0:

            if num%6==0:
                num=acumulado+num
                acumulado=num
                print(acumulado)
            elif num%9==0:
                num=acumulado*num
                acumulado=num
                print(acumulado)
            elif num%7==0:
                num=acumulado-num
                acumulado=num
                print(acumulado)
            elif num%5==0:
                num=acumulado/num
                acumulado=num
                print(acumulado)
            else:
                acumulado=num
                print(acumulado)

        
