# Escriba un programa en Python que le solicite al usuario la información de una matriz de tamaño NxM con elementos enteros. El programa debe sumar cada uno de los elementos de la matriz y mostrar el resultado.

def main():
    N = eval(input("Digite el número de filas: "))
    M = eval(input("Digite el número de columnas: "))
    matrizNumeros = crearMatriz(N,M)
    print(matrizNumeros)
    suma = acumuladorDatos(matrizNumeros, N,M)
    print(suma)

def crearMatriz(N,M):
    matriz = []
    for i in range(0, N):
        lista = []
        for j in range(0,M):
            dato = eval(input("Digite el dato: "))
            lista.append(dato)
        matriz.append(lista)            
    return matriz

def acumuladorDatos(matriz, N, M):
    acumulador = 0
    for i in range(0,N):
        for j in range(0,M):
            acumulador += matriz[i][j]
    return acumulador
    
main()