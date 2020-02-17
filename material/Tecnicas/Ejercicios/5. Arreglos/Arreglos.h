#define SIZE 10
#include <stdio.h>

void presentarArreglos();

/*Imprime de la posición 0 hasta la última posición de un arreglo de valores enteros. */
void imprimirArreglo(int arreglo[], int tam);

/*LLena de la posición 0 hasta la última posición de un arreglo de valores enteros 
que son pedidos por consola*/
void llenarArreglo(int arreglo[], int tam);

/* Recibe por parámetros un arreglo y su tamaño y luego muestra los números que 
se encuentran en las posiciones impares*/
void mostrarImpares(int arreglo[], int tam);

/* Busca el valor en el arreglo y si se encuentra retorna 1, 
de lo contrario retorna 0*/
int tieneValor(int arreglo[], int tam, int num);

/* Ordena un arreglo entero con el metodo burbuja */
void ordenarBurbuja(int arreglo[], int tam);

