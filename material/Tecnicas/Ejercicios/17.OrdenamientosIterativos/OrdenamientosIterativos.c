#include "OrdenamientosIterativos.h"

void imprimirOrdenAscendente(int arreglo[], int size) {
	int i = 0;
	for (i = 0; i < size; i++) {
		printf("Posicion: %d -- Valor: %d \n", i, arreglo[i]);
	}
}


void intercambiar(int arreglo[], int posicion1, int posicion2) {
	//Intercambiar en el arreglo lo que esta en la posicion1 
	//con lo que esta en la posicion2
	
	


}

void ordenarBurbujaBasicoAscendente(int arreglo[], int size) {
	int i, j, numIteraciones=0;
	//Completar condiciones FOR
	for (i = 1;    ; i++) {
		for (j = 0;    ; j++) {
			numIteraciones++;
			//Completar
			if (              ) {
				//Llamar a la operación intercambiar


			}
		}
	}
	printf("Numero de iteraciones del algoritmo %d: \n" , 
		numIteraciones);
}

void ordenarBurbujaBasicoDescendente(int arreglo[], int size) {
	
	//Completar
}

void ordenarBurbujaBandera(int arreglo[], int size) {
	int i, j, numIteraciones=0, ordenado=0;
	i=1;
	while( i <= size && ordenado==0){
		ordenado=1; //Se inicia en 1 para asumir que está ordenado
		for (j = 0; j < size-1; j++) {
			numIteraciones++;
			if (                      ) {
				
				//Completar
			}
		}
		i++;
	}
	printf("Numero de iteraciones del algoritmo %d: \n" , 
		numIteraciones);
}



void ordenarSeleccion(int arreglo[], int size) {
	int i, j, posMinima,numIteraciones=0;
	for (i = 0; i < size - 1; i++) {
		//Indica la posicion del menor de todos los elementos
		posMinima = i;
		//Se inicia j una posición adelante de la i para
		// no comparar dos veces el mismo campo
		for (j = i + 1; j < size; j++) {		
			//Para ordenamiento ascendente. 
			//Si el valor del arreglo en la posición J es mayor
			//al de la posición i, entonces la posición j es el nuevo
			//elemento de la posMinima. 
			//Completar



			numIteraciones++;
		}
		//Si hubo cambios en la posicion
		if (i != posMinima) {
			intercambiar(arreglo, i, posMinima);
		}
		
	}
	printf("Numero de iteraciones %d \n", numIteraciones);
}

void ordernarInsercion(int arreglo[], int size) {

	int i, j, temp;
	for (i = 1; i < size; i++) {
		//temp= elemento a ubicar correctamente
		temp = arreglo[i];
		//Subindice del elemento que se quiere ubicar correctamente
		j = i;
		while (temp < arreglo[j - 1] && j > 0) {
			//Se mueven los elementos que se necesiten del arreglo hacia adelante
			arreglo[j] = arreglo[j - 1];
			j--;
		}
		//Se ubica el temp en la posicion correcta
		arreglo[j] = temp;
	}
}

/* Completar */
void ordernarInsercionV2(int arreglo[], int size) {

	int i, j, temp;
	for (i = 1; i < size; i++) {
		//temp= elemento a ubicar correctamente
		temp = arreglo[i];
		//Subindice del elemento que se quiere ubicar correctamente
		j = i-1;
		while (                           ) {
			//Se mueven los elementos que se necesiten del arreglo 
			// hacia adelante
			
		}
		//Se ubica el temp en la posicion correcta
		
	}
}
