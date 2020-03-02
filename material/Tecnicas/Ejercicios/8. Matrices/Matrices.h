#include <stdio.h>


void llenarMatriz(int matriz [][4] , int fil, int col); 
//El tamaño de las columnas siempre se debe enviar como parámetro
void mostrarMatriz(int matriz [][4] , int fil, int col); 

//Imprime la matriz usando aritmetica de punteros
void mostrarMatrizAritmPunt(int matriz [][4] , int fil, int col); 
//Retorna 1 si la matriz es cuadrada y 0 si la matriz no es cuadrada
int esCuadrada(int matriz [][4] , int fil, int col); 
//Muestra la diagonal de una matriz, si la matriz es cuadrada
int mostrarDiagonal(int matriz [][4] , int fil); 
//Muestra la matriz iniciando con j en la posicion columnas-1 e i en la posicion fila -1
void imprimirAlReves(int matriz [][4] , int fil, int col);
//Muestra la matriz iniciando con j en la columna 0 e i en la posicion fila -1
void imprimirFilaFinalColumnaFinal(int matriz [][4] , int fil, int col);
//Muestra la matriz iniciando con j en la posicion columnas-1  e i en la posicion 0
void imprimirFilaInicialColumnaFinal(int matriz [][4] , int fil, int col);
//Transponer matriz. Si la matriz es cuadrada intercambia las filas con las columnas
void transponerMatriz(int matriz [][4] , int fil, int col);