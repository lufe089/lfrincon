# Escriba un programa en Python que le solicite al usuario por pantalla un listado de números (para finalizar debe ingresar 0). Cree un diccionario en donde se almacene la siguiente información a partir de los números ingresados:
# Cantidad de números pares
# Cantidad de números impares
# Número mayor
# Número menor
# Promedio

def main():
    informacion = {}
    listaUsuario = solicitarNumeros()
    numerosPares = cantidadPares(listaUsuario)
    numerosImpares = cantidadImpares(listaUsuario)
    informacion["cantidadPares"] = numerosPares
    informacion["cantidadImpares"] = numerosImpares
    informacion["numeroMayor"] = max(listaUsuario)
    informacion["numeroMenor"] = min(listaUsuario)
    informacion["promedio"] = promedioLista(listaUsuario)
    print(informacion)

def solicitarNumeros():
    listaNumero = []
    numeroUsuario = eval(input("Digite un número: "))
    while numeroUsuario != 0:
        listaNumero.append(numeroUsuario)
        numeroUsuario = eval(input("Digite un número: "))
    return listaNumero

def cantidadPares(lista):
    contadorPares = 0
    for elemento in lista:
        if elemento % 2 == 0:
            contadorPares += 1
    return contadorPares

def cantidadImpares(lista):
    contadorImpares = 0
    for elemento in lista:
        if elemento % 2 != 0:
            contadorImpares += 1
    return contadorImpares

def promedioLista(lista):
    cantidadElementos = len(lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    promedio = acumulador/cantidadElementos
    return promedio

main()