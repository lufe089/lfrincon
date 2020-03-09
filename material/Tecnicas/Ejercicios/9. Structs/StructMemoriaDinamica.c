#include "Structs.h"

struct Fish * llenarFishMemDinamica() {
	//Se reserva el tamaño de lo que va a apuntar pFish
	fish_t * pFish = malloc(sizeof(fish_t));
	if (pFish != NULL) {
		printf("ingrese un nombre para el pez max 24 caracteres\n");
		fgets(pFish->nombre,25,stdin);
		//TODO llene la especie, el número de dientes, la edad 
		//Recuerde usar la función flush_in luego de que lea un
		// numero y quiera leer una cadena. 
		
		return pFish;
	}else{
		return NULL;
	}
}

/* Se recibe la direccion de la estructura y no su valor para impresion
	podría usarse tambien fish_t * pFish

*/
void imprimirDatosPasoReferencia(struct Fish * pFish){
	printf(".......\n......");
	printf("Nombre pez:%s \n", pFish->nombre );
	//TODO: imprima el resto de valores
}
