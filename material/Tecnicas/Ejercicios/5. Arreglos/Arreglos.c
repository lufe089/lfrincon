#include "Arreglos.h"

void presentarArreglos(){
	int arreglo [SIZE];
	int i;
	//LLenar arreglo
	for(i=0; i< SIZE; i++){
		arreglo[i]=i;
	}
	//Imprimir valores
	for( i=0; i< SIZE; i++){
		printf (" valor %d \n",arreglo[i]);
	}
}

/* Completar */