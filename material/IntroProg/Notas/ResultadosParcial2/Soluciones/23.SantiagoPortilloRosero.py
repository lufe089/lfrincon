#SantiagoPortilloRosero
#Sondeo - Hospital de mascotas
conjuntos=int(input("Ingrese el número de conjuntos: "))
apartamentos=int(input("Ingrese el número de apartamentos: "))
cont=0
ac=0
suma=0
mascotas=0
while cont<conjuntos:
    contt= 0
    while contt<apartamentos:
        mascotas=int(input("Ingrese el número de mascotas que tiene: "))
        if mascotas>=3:
            ac+=1
        contt += 1
    cont += 1
    mascotas += mascotas  # Esta variable no te sirve pq la volviste el input.
print("El número de apartamentos que tiene tres mascotas o más es", ac)


#Multicalculadora

acumulado=0
n=0
bandera = False
while n!= 1:
    n=int(input("Ingrese un número entero: "))
    acumulado=n
    if acumulado<n:
        menor= n
        print("El menor numero fue", menor)
    while n!=0:
        if n%12==0:
            acumulado =(n+acumulado)
        elif n%9==0:
            acumulado = n*acumulado
        elif n%7==0:
            acumulado = n-acumulado
        elif n%5==0:
            acumulado = n/acumulado
        bandera== True
        print(acumulado)

#VivaAir
def f_calculoBase():
    dist=int(input("Cuantos kilometros hay hacia su destino?: "))
    tiempo=int(input("Cuanto durá su vuelo?: "))
    modalidad=int(input("Cual es su modalidad de tiquete?" " " "Si es a la carta = 1, si es combo+ = 2, si es combo++ =3: "))
    if modalidad == 1:
        tiquete = 65000
        km=100
        valor_base=(dist/km)*tiquete
        print("Su tiquete es de", valor_base)
    elif modalidad == 2:
        tiquete =25000
        km=70
        pc=30
        aumenta=10000
        valor_base= (dist/ km)*tiquete + (tiempo/pc)*aumenta
        print("Su tiquete es de", valor_base)
    elif modalidad==3:
        tiquete =25000
        km=70
        pc=60
        aumenta=10000
        valor_base= (dist/ km)*tiquete + (tiempo/pc)*aumenta
        print("Su tiquete es de", valor_base)
    return valor_base

def f_costoAdicional():
    maletasbod=int(input("Numero de maletas en bodega: "))
    tvuelo=input("Es vuelo nacional o internacional: ")
    if tvuelo== "nacional":
        vad=(70000*maletasbod)
    elif tvuelo== "internacional":
        vad=(250000*maletasbod)
    print("El valor adicional es de", vad)
    formaDePago=input("Escriba su forma de pago: ")
    if formaDePago == "internet":
            vad = (vad*0.7)
            print("Su nuevo valor adicional con el 70% de descuento es de:", vad)


p_calculoTiquete=(f_calculoBase())
f_costoAdicional()
print("El valor que deberá pagar es de", (valor_base+vad))
