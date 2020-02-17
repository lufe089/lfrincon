#define SIZE 10
#include <stdio.h>

/* EJEMPLOS */

/*Imprime de la posición 0 hasta la última posición de un arreglo de valores enteros. */
void imprimirArregloAritmeticaPunteros(int arreglo[], int tam);

/* Recibe por parámetros dos arreglos y sus tamaños y calcula la diferencia
del arreglo del primer parametro con el arreglo del segundo parametro.
Usa aritmética de punteros. El tercer arreglo de parametros corresponde al arreglo en el que
se guardará la diferencia y el tamanio real del arreglo diferencia se puede obtener
del parametro tamDiferencia que es un apuntador al tamaño con el que queda el arreglo diferencia */
void calcularDiferenciaArreglos(int arregloUno[], int arregloDos[], int arregloDiferencia[] , int tam1, int tam2, int* tamDiferencia);

/*LLena de la posición 0 hasta la última posición de un arreglo de valores enteros 
que son pedidos por consola*/
void llenarArregloAritmeticaPunteros(int arreglo[], int tam, int semilla);


/* EJERCICIOS */



/* Recibe por parámetros dos arreglos y sus tamaños y calcula la intersección
de ambos arreglos.
Usa aritmética de punteros. El tercer arreglo de parametros corresponde al arreglo en el que
se guardará la intersección y el tamanio real de la intersección se puede obtener
del parametro tamIntersec que es un apuntador al tamaño real con el que queda el arreglo intersección
al terminar la operación. */
void calcularInterseccionArreglos(int arregloUno[], int arregloDos[], int[] arregloInterseccion, int tam1, int tam2, int* tamIntersec);

/* Recibe por parámetros dos arreglos y sus tamaños y calcula la unión
de ambos arreglos.
Usa aritmética de punteros. La función 
retorna el arreglo unión y el tamaño real del arreglo unión se puede obtener
del parametro tamUnion que es un apuntador al tamaño con el que queda el arreglo unión al terminar
la operación. */

void calcularUnion(int arregloUno[], int arregloDos[], int[] arregloUnion, int tam1, int tam2, int* tamUnion);


