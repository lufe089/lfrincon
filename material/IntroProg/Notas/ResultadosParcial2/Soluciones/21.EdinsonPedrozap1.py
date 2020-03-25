#punto1
n=int(input("Digite la cantidad de conjuntos residenciales: "))
cont=1
contcm=0
sumascota=0
contapartamento=0
while cont<=n:
    contmascota = 0
    m=int(input("Digite la cantidad de apartamentos del conjunto: "))
    while contmascota<m:
        mascota=int(input("Digite cuantas mascotas tiene: "))
        contcm+=1
        contmascota+=1
        sumascota+=mascota
    print("conjunto ",cont,":")
    contap = 0
    while contap<mascota:
        contapartamento+=1
        print("apto", contapartamento, ": ", mascota)
        contap+=1
    print(contmascota,"apartamentos poseen mascotas")
    print("El conjunto ",cont," tiene",sumascota,"mascotas")
    cont+=1

#punto2
num = int(input("Ingrese un numero: "))
cont = 1
acum = 0
while cont <= num:
    if num / cont == 6:
        acum = num + (num/6)
    elif (num / cont) == 9:
        acum = num * (num/9)
    elif (num / cont) == 7:
        acum = num - (num/7)
    elif (num / cont) == 5:
        acum = num / (num/5)
    if acum == 0:
        acum += num
    elif num==-1:
        break
    cont += 1
print("El acumulado es: ",acum)











