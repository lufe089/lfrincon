#CARLOS ALBERTO BURGOS AVENDAÑO
#Punto Uno
conjuntos=int(input("Ingrese el numero de conjuntos del barrio: "))
contconjuntos=0
ceromascotas=0
while contconjuntos<conjuntos:
    nombre=input("Cual es el nombre del conjunto: ")
    aptos=int(input("Cuantos apartamentos tiene este conjunto?"))
    contaptos=0
    contmascotas=0
    while contaptos<aptos:
        mascotas=int(input("Cuantas mascotas hay en este apartamento?"))
        if mascotas==0:
           ceromascotas+=1
        else:
           contmascotas+=mascotas
        contaptos+=1
    print("Este conjunto tiene",contmascotas,"mascotas")
    contconjuntos+=1
print("Esto conjuntos tienen",ceromascotas,"aptos con cero mascotas")

#Punto Dos
acumulado=0
num=0
var=True
while num!=-1:
    numero=int(input("Ingrese el valor a calcular: "))
    if var==True:
        acumulado=numero
        var=False
    if numero%4==0:
        acumulado=acumulado+numero
    if numero%9==0:
        acumulado=acumulado*numero
    if numero%7==0:
        acumulado=acumulado-numero
    if numero%5==0:
        acumulado=acumulado/numero
    if not(numero%4==0 and numero%9==0 and numero%7==0 and numero%5==0):
        acumulado=acumulado
    num=numero
print(acumulado)

#Punto Tres
def f_calculoBase(Distancia,Minutos,Modalidad):
    valorbase=0
    if Modalidad=="A la carta":
      valorbase=((Distancia/100)*100000)
    elif Modalidad=="Combo+":
      valorbase=((Distancia/70)*25000)+((Minutos/30)*10000)
    elif Modalidad=="Combo++":
      valorbase=((Distancia/50)*25000)+((Minutos/60)*10000)
    return valorbase

def f_costoAdicional(FormaPago,Modalidad,cantMaletas,DesVuelo):
    valoradicional=0
    if DesVuelo=="Nacional":
        if Modalidad=="A la carta" and cantMaletas>0:
          valoradiconal+=70000
        elif Modalidad=="Combo+" and cantMaletas>1:
          valoradicional+=70000
        elif Modalidad=="Combo++" and cantMaletas>2:
          valoradicional+=70000   
    elif DesVuelo=="Internacional":
        if Modalidad=="A la carta" and cantMaletas>0:
          valoradiconal+=250000
        elif Modalidad=="Combo+" and cantMaletas>1:
          valoradicional+=250000
        elif Modalidad=="Combo++" and cantMaletas>2:
          valoradicional+=250000
    if FormaPago=="Internet":
        valoradicional=0.7*(valoradicional)
    elif FormasPago=="Otros":
        valoradicional=valoradicional
    return valoradicional

def CostoTiquete():
  Nombre=input("Digite su nombre señor: ")
  Distancia=int(input("Ingrese la distancia del vuelo en kilometros: "))
  Minutos=int(input("Ingrese la duracion del vuelo en minutos: "))
  Modalidad=input("Ingrese la Tarifa Seleccionada (A la carta, Combo+, Combo++): ")
  FormaPago=input("Ingrese la Modalidad de Pago, por internet u otros: ")
  cantMaletas=int(input("Ingrese la cantidad de maletas va llevar en bodega: "))
  DesVuelo=input("Ingrese si el vuelo es Nacional o Internacional: ")
  ValorIncial=f_calculoBase(Distancia,Minutos,Modalidad)
  ValorExtras=f_costoAdicional(FormaPago,Modalidad,cantMaletas,DesVuelo)
  ValorTiquete=ValorIncial+ValorExtras
  print("Sr o Sra",Nombre,"el costo de su vuelo es de",ValorTiquete)

CostoTiquete()

    
    
    
