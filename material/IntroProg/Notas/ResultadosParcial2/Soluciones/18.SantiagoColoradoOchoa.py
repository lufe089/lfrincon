#SantiagoColoradoOchoa - Ing.Electrónica - 2020-1.
#MULTICALCULADORA.
def multicalculadora():
    acumulado=0
    print("Ingrese '-1' si desea terminar el cálculo.")
    entranteant=9999999999**9
    menor=0
    entrante=0
    while entrante!=-1:
        entrante=int(input("Ingrese un número: "))
        if acumulado==0:
            acumulado=entrante
        else:
            if entrante%12==0:
                acumulado=acumulado+entrante
            elif entrante%9==0:
                acumulado= acumulado*entrante
            elif entrante%7==0:
                acumulado=acumulado-entrante
            elif entrante%5==0:
                acumulado=acumulado/entrante
            elif entrante!=0:
                acumulado=acumulado
        if entrante!=-1 and entrante<=entranteant:
            menor=entrante
        entranteant = entrante
    print("El acumulado es", acumulado)
    print("El menor numero ingresado fue", menor)
multicalculadora()
#HOSPITAL_DE_MASCOTAS.
def HospitalDeMascotas():
    conjuntos=int(input("Ingrese la cantidad de conjuntos encuestados: "))
    cont=1
    mayoigutres = 0
    apartamentosacu=0
    while cont<=conjuntos:
        contmascotas=0
        apartamentos=int(input("          Ingrese la cantidad de apartamentos del conjunto: "))
        apartamentosacu = apartamentosacu+apartamentos
        cont1=1
        while cont1<=apartamentos:
            mascotas=int(input("                    Ingrese la cantidad de mascotas del apartamento: "))
            if mascotas>=3:
                mayoigutres+=1
            contmascotas=contmascotas+mascotas
            cont1+=1
        print("El conjunto", cont, "tiene", contmascotas, "mascotas en total.")
        cont+=1
    print("De los", apartamentosacu, "apartamentos encuestados", mayoigutres, "tienen 3 o más mascotas. ")
HospitalDeMascotas()
#VIVA_AIR.
def vivaAir():
    def f_calculoTiquete():
        valor_final=0
        nombre=input("Ingrese su nombre: ")
        print("Se le pedirá que ingrese la modalidad de precio escogida.")
        print("     Ingrese 1 si la modalidad escogida fue 'A la carta'.")
        print("     Ingrese 2 si la modalidad escogida fue 'Combo+'.")
        print("     Ingrese 3 si la modalidad escogida fue 'Combo++'.")
        modalidad=int(input("Modalidad escogida: "))
        print("Se le pedirá que ingrese si su vuelo es nacional o internacional.")
        print("     Ingrese 1 si su vuelo es nacional.")
        print("     Ingrese 2 si su vuelo es internacional.")
        destino=int(input("¿Nacional o internacional?: "))
        print("¿Realizó su compra por internet?")
        print("     Ingrese 1 si lo hizo.")
        print("     Ingrese 2 si no lo hizo.")
        compra=int(input("Ingrese aquí el número: "))
        print("A continuación ingrese la distancia que recorre su vuelo en kilometros.")
        distancia=int(input("Distancia que va a volar: "))
        print("A continuación ingrese el tiempo estimado de vuelo en minutos.")
        tiempo=int(input("Tiempo estimado de vuelo: "))
        print("Por último, ingrese la cantidad de maletas adicionales en bodega que va a llevar.")
        maletas=int(input("Maletas adicionales: "))
        valor_base= f_calculoBase(modalidad, distancia, tiempo)
        valor_adicional= f_costoAdicional(compra, maletas, destino)
        valor_final=valor_base+valor_adicional
        print("Señor(a)", nombre, "el valor final de su tiquete es de", valor_final, "pesos colombianos.")
    def f_calculoBase(modalidad, distancia, tiempo):
        valor_base=0
        if modalidad==1:
            valor_base=(65000*(distancia/100))
        elif modalidad==2:
            valor_base=((distancia/70)*25000)+((tiempo/30)*10000)
        elif modalidad==3:
            valor_base=((distancia/50)*25000)+((tiempo/60)*10000)
        return valor_base
    def f_costoAdicional(compra, maletas, destino):
        valor_adicional=0
        if destino==1:
            if compra==1:
                valor_adicional = 0.7 * (maletas*70000)
            elif compra==2:
                valor_adicional = maletas*70000
        elif destino==2:
            if compra==1:
                valor_adicional = 0.7 * (maletas*250000)
            elif compra==2:
                valor_adicional = maletas*250000
        #NO AGREGUÉ LA MODALIDAD PORQUE DESDE UN PRINCIPIO SE PODÍA SOLO PEDIR LA CANTIDAD DE MALETAS ADICIONALES A LAS INCLUIDAS EN LA MODALIDAD.
        return valor_adicional
    print("ESTIMADO CLIENTE, RECUERDE SER CLARO CUANDO DIGITE LOS VALORES QUE LE PIDA EL PROGRAMA.")
    print("SI EL VALOR FINAL DE SU TIQUETE NO ES UN NÚMERO ENTERO DEBE REDONDEARLO AL VALOR MÁS CERCANO.")
    f_calculoTiquete()
vivaAir()
