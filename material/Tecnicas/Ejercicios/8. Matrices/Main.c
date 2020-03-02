#include "Matrices.h"

void mostrarMenu() {
	int opcion = 0;
	int filas=2, columnas=4;
	int matriz[filas][columnas];
	int matrizListCompl[2][4] = { { 1, 2, 10, 12 }, { 3, 4, 98, 65} };
	int matrizListInic[2][4] = { { 1, 2 }, { 3, 4} };
	int matrizCero[2][4] = { { 0 }, { 0} };
	do {
		printf(" Opciones para matrices \n\n");
		printf("1. LLenar matriz\n");
		printf("2. Mostrar matriz\n");
		printf("3. Imprimir al reves\n");
		printf("4. Imprimir columnaCero filaTres\n");
		printf("-1. Salir\n\n");
		printf(" Opc: ");
		scanf("%d", &opcion);
		switch (opcion) {
			case 1:
				llenarMatriz(matriz,filas,columnas);
				break;
			case 2:
				mostrarMatriz(matrizCero,filas,columnas);
				break;
			case 3:
				imprimirAlReves(matrizListCompl,filas,columnas);
				break;
		
		}
		//Cuando el usuario ingrese -1 se terminará el while y se terminará el menu
	} while(opcion!=-1);
}



int main()
{
	//Menu que muestra las opciones disponibles
	mostrarMenu ();
	return 0;
}
