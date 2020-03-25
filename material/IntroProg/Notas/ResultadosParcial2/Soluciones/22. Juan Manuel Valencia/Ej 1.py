#Juan Manuel Valencia
N_conjuntos=0
M_aptos=0
cont_apt=0
cont_conj=0
Num_pet=0
suma_mascotas=0
N_conjuntos=int(input("Ingrese el número de conjuntos"))
while N_conjuntos>0:
    M_aptos=int(input("Ingrese el número de apartamentos"))
    while M_aptos>0:
        Num_pet=int(input("Ingrese el número de mascotas"))
        suma_mascotas+=Num_pet
        M_aptos-=1
        if Num_pet==2:
            cont_apt+=1
    N_conjuntos-=1
print (suma_mascotas, "Fue el total de mascotas")
print(cont_apt,  "Fue el total de apartamentos con dos mascotas")
