#include "Arreglos.h"


/* EJEMPLOS */
void imprimirArregloAritmeticaPunteros(int arreglo[], int tam){
	int i;
	for (i = 0; i < tam; ++i){
		printf("valor de %d es %d\n",i, *(arreglo+i));
	}

}

void llenarArreglo(int arreglo[], int tam, int semilla){
	int i;
	for (i = 0; i < tam; ++i){
		//Llena el arreglos con números consecutivos 
		// más el valor recibido en semilla.
		*(arreglo + i) = i+semilla;
	}
}

/* Recibe por parámetros dos arreglos y sus tamaños y calcula la diferencia
del arreglo del primer parametro con el arreglo del segundo parametro.
Usa aritmética de punteros. El tercer arreglo de parametros corresponde al arreglo en el que
se guardará la diferencia y el tamanio real del arreglo diferencia se puede obtener
del parametro tamDiferencia que es un apuntador al tamaño con el que queda el arreglo diferencia */
void calcularDiferenciaArreglos(int arregloUno[], int arregloDos[], int arregloDiferencia[], int tam1, int tam2, int * tamDiferencia){

	int arregloResultado[tam1];
	int estaValor=0; // 0 no está el valor 1 si está
	int i, j;

	for( i=0; i< tam1; i++){
		estaValor==0;
		for(j=0;j<tam2 && estaValor==0;j++){
			//Cuando ambos valores son iguales se cambia la variable bandera de estado. 
			//Se usa aritmetica de punteros 
			// Equivalente a arregloUno[i] == arregloDos[j]
			if(*(arregloUno+i) == *(arregloDos+j)){
				//Se cambia la bandera para interrumpir el ciclo
				estaValor=1;
			}
		}
		if(estaValor==1){
			// Usando aritmética de punteros se asigna a al arreglo resultado el valor de arregloUno en la posicion i
			// Se usa el * en tamDiferencia porque tamDiferencia es un apuntador y aquí se necesita el contenido de esa dirección que es donde
			// se va guardando la posición

			// Equivalente a arregloDiferencia[*tamDiferencia] == arregloUno[i]
			*(arregloDiferencia + (*tamDiferencia)) = *(arregloUno+i);
			(*tamDiferencia)++;
		}
	}
}



