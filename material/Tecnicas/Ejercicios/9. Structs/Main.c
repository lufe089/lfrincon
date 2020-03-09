#include "Structs.h"

int main()
{
	
	struct Fish pirana1 = {"Snappy", "Piranha", 69, 4};
	struct Fish arregloPiranitas[5];
	struct Fish pirana2;
	pirana2=llenarFishTypeDef();
	printf("Pirana 1 \n");
	imprimirDatosPasoValor(pirana1);

	printf("Pirana 2\n");
	imprimirDatosPasoValor(pirana2);

	//TODO: Llamar a imprimir usando la función del paso por referencia


	//Pruebas paso por referencia y memoria dinámica
	// Equivalente a decir fish_t *pFish= (fish_t*) llenarFishMemDinamica();
	fish_t * pFish= (fish_t *) llenarFishMemDinamica();
	
	//Imprimir usando la función para paso por referencia
	imprimirDatosPasoReferencia(pFish);
	
	//TODO: Llamar a imprimir usando la función del paso por valor


	//Se libera la memoria de pFIsh
	free(pFish);

	return 0;
}
