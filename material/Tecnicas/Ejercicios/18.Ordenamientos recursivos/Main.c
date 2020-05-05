#include "OrdenamientoRecursivo.h"


int main() {
	//int arreglo[TAM_ARREGLO] = { 6, 5, 3, 1, 2, -9 };
	int arreglo[TAM_ARREGLO] = { 0,-2, 100,-1, 3, 1 };
	imprimirAscendente(arreglo, TAM_ARREGLO);

	quickSort(arreglo, 0, TAM_ARREGLO-1);
	printf("Algoritmo ordenado  \n");
	imprimirAscendente(arreglo, TAM_ARREGLO);

	return 0;
}

