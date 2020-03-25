#sección 1
n=int(input("Número de conjuntos: "))
contn=1
mascotas_conjunto=0
while contn<=n:
    m=int(input("Número de apartamentos: "))
    print("Conjunto ",contn)
    contm=1
    aptos_una_mascota=0
    mascotas_apto=0
    while contm<=m:
        mascotas=int(input("¿Cuántas mascotas posee? si no tiene mascotas por favor responda con el número 0: "))
        if mascotas==1:
            aptos_una_mascota+=1
        mascotas_apto+=mascotas
        print("Apto ",contm,": ",mascotas_apto)
        contm+=1
        
    mascotas_conjunto+=mascotas_apto
    print("Mascotas por conjunto: ",mascotas_conjunto)
    contn+=1

#sección 2
acum=0
bandera=False
mayor=0
menor=0
num=0
while num!=-1:
    num=int(input("Ingrese un número entero: "))
    if acum==0:
        acum=num
        print(acum)
    elif num%6==0:
        acum=num+acum
        print(acum)
    elif num%9==0:
        acum=num*acum
        print(acum)
    elif num%7==0:
        acum=acum-num
        print(acum)
    elif num%5==0:
        acum=acum/num
        print(acum)

    if bandera==False:
        mayor==num
        menor==num
        bandera=True
    if num<menor:
        menor=num
    elif num>mayor:
        mayor=num
        


print("El acumulado es: ",acum)
print("El número más pequeño es: ",menor)

#ESTE CÓDIGO NO FUNCIONA
#sección 3
#5
def f_calculoBase(km,minutos,modalidad):
    if modalidad=="a la carta":
        valor_base=(km/100)*45000
    elif modalidad=="combo+":
        valor_base=(km/100)*45000+(minutos/30)*10000
    elif modalidad=="combo++":
        valor_base=(km/50)*25000+(minutos/60)*10000
    return valor_base

#1
def f_costoAdicional(forma_pago,modalidad,cantidad_maletas,tipo_vuelo):
    valor_base=f_calculoBase(km,minutos,modalidad)
    if cantidad_maletas>1:
        if forma_pago=="internet":
            if tipo_vuelo=="nacional":
                valor_adicional=(valor_base-(valor_base*0.3))+(70000*cantidad_maletas)
            elif tipo_vuelo=="internacional":
                valor_adicional=(valor_base-(valor_base*0.3))+(250000*cantidad_maletas)
        elif forma_pago=="normal":
            if tipo_vuelo=="nacional":
                valor_adicional=valor_base+(70000*cantidad_maletas)
            elif tipo_vuelo=="internacional":
                valor_adicional=valor_base+(250000*cantidad_maletas)
        
    return valor_adicional


# 4
def p_calculoTiquete(f_calculoBase,f_costoAdicional):
    nombre=input("Nombre: ")
    km=float(input("Distancia al destino en km: "))
    minutos=int(input("¿Cuántos minutos se demora el vuelo?: "))
    modalidad=input("Escoja la modalidad (a la carta, combo+ ó combo++): ")
    forma_pago=input("¿Cuál es la forma de pago? (internet o normal): ")
    cantidad_maletas=int(input("Cantidad de maletas: "))
    tipo_vuelo=input("Tipo de vuelo (nacional o internacional): ")
    
    f_calculoBase=f_calculoBase(km,minutos,modalidad)
    f_costoAdicional=f_costoAdicional(forma_pago,modalidad,cantidad_maletas,tipo_vuelo)
    
    valor_final=f_calculoBase+f_costoAdicional
    
    print("Señor(a) ",nombre," el valor final de su tiquete es de ",valor_final)

p_calculoTiquete(f_calculoBase,f_costoAdicional)



