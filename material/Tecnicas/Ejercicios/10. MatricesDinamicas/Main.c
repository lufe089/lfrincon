#include "MatricesDinamicas.h"

void mostrarMenu() {
	int opcion = 0;
	
	do {
		printf(" Opciones para matrices \n\n");
		printf("1. Completar con las opciones\n");
		printf("-1. Salir\n\n");
		printf(" Opc: ");
		scanf("%d", &opcion);
		switch (opcion) {
			case 1:
				break;
		
		}
		//Cuando el usuario ingrese -1 se terminará el while y se terminará el menu
	} while(opcion!=-1);
}



int main()
{
	int filas=2, columnas=4;
	int ** pMatriz; //Apuntador doble a la dirección de memoria que se reserva para ubicar la matriz

	//Se llama a la operacion que reserva la memoria
	pMatriz= reservarMemoriaMatriz(filas, columnas);
	if(pMatriz!=NULL){
		//Menu que muestra las opciones disponibles
		mostrarMenu ();
	}else{
		printf("No se pudo reservar espacio en memoria para esta matriz");
	}
	return 0;
}
