#include "OrdenamientosIterativos.h"


int main() {

	int arreglo[TAM_ARREGLO] = { 6, 5, 3, 1, 8, 7,2, 4 };
	//int arreglo[TAM_ARREGLO] = { 1, 2, 3, 4, 5, 6, 7, 8 };

	/* Impresión antes del ordenamiento*/
	imprimirOrdenAscendente(arreglo, TAM_ARREGLO);

	/*Descomentar para ir probando cada uno de los algoritmos */
	ordenarBurbujaBasicoAscendente(arreglo, TAM_ARREGLO);
	//ordenarBurbujaBandera(arreglo, TAM_ARREGLO);
	//ordenarSeleccion(arreglo,TAM_ARREGLO);
	//ordernarInsercion(arreglo, TAM_ARREGLO);

	printf("Algoritmo ordenado  \n");
	imprimirOrdenAscendente(arreglo, TAM_ARREGLO);

	return 0;
}

