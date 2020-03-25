def multiCalculadora(numOpcional):
    acumulado = 0
    numUsuario = 0
    primerMenor = False
    menor = 0
    while numUsuario !=- 1:
        numUsuario = int(input("Ingrese el numero "))
        # Inicio el menor la primera vez
        if primerMenor == False:
            menor= numUsuario
            primerMenor = True

        # Actualizar el menor
        if numUsuario < menor and numUsuario !=-1:
            menor=numUsuario

        if acumulado == 0:
            acumulado += numUsuario
        else:
            if numUsuario % numOpcional == 0:
                acumulado += numUsuario
            elif numUsuario % 9 == 0:
                acumulado *= numUsuario
            elif numUsuario % 7 == 0:
                acumulado -= numUsuario
            elif numUsuario % 5 == 0:
                acumulado /= numUsuario
    print ("El acumulado es:", acumulado )
    print("El menor es", menor)


def multiCalculadoraLista(numOpcional, todos):
    acumulado = 0
    numUsuario = 0
    for numUsuario in todos:
        if acumulado == 0:
            acumulado += numUsuario
        else:
            if numUsuario % numOpcional == 0:
                acumulado += numUsuario
            elif numUsuario % 9 == 0:
                acumulado *= numUsuario
            elif numUsuario % 7 == 0:
                acumulado -= numUsuario
            elif numUsuario % 5 == 0:
                acumulado /= numUsuario
        print("Acumulado parcial", acumulado)
    print ("El acumulado es:", acumulado )

print ("Valores que son múltiplos para todos")
todos = [23,27,21,5,19,24]
print("Con cuatro")
multiCalculadoraLista(4, todos)
print("Con seis")
multiCalculadoraLista(6, todos)
print("Con ocho")
multiCalculadoraLista(8, todos)
print("Con doce")
multiCalculadoraLista(12, todos)


print ("\nCambiando los valores")
todos = [23,27,21,5,19,24,4,6,8,12]
print("Con cuatro")
multiCalculadoraLista(4, todos)

print("Con seis")
multiCalculadoraLista(6, todos)

print("Con ocho")
multiCalculadoraLista(8, todos)

print("Con dotoce")
multiCalculadoraLista(12, todos)
