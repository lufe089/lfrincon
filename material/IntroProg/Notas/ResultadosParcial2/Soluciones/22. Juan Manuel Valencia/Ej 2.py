#Juan Manuel Valencia
Num_entero=0
Suma1=0
Total_suma=0
while Num_entero!=-1:
    Num_entero=int(input("Ingrese un número entero"))
    if Total_suma ==0:
     Total_suma+=Num_entero
     print(Total_suma)
    elif Total_suma !=0:
        if Num_entero//8==0:
            Total_suma+=Num_entero
            print(Total_suma)
        elif Num_entero//9==0:
            Total_suma=Total_suma*Num_entero
            print(Total_suma)
        elif Num_entero//7==0:
            Total_suma=Total_suma-Num_entero
            print(Total_suma)
        elif Num_entero//5==0:
            Total_suma/Num_entero
        else:
            Total_suma=Total_suma
print(Total_suma)

    
