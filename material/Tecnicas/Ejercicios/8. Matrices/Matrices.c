#include "Matrices.h"

void llenarMatriz(int matriz [][4],  int fil, int col) {
	int i,j;
	for (i = 0; i < fil; i++) {
		for (j = 0; j < col; j++) {
			printf("Ingrese un numero un numero ");
			scanf("%d", &matriz[i][j]);
		}
	}
}

void mostrarMatriz(int matriz [][4],  int fil, int col) {
	int i,j;
	for (i = 0; i < fil; i++) {
		for (j = 0; j < col; j++) {
			printf(" %d ",matriz[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void imprimirAlReves(int matriz [][4] , int fil, int col){
	int i,j;
	for (i = fil-1; i >= 0; i--) {
		for (j = col-1; j >= 0; j--) {
			printf(" %d ",matriz[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}