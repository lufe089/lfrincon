#include "Apuntadores.h"

/* Operacion de ejemplo */
void dividir (int* pNum1, int* pNum2, float *pResultado){

	//Se hacen las operaciones con el contenido de los apuntadores pNum1, pNum2, pResultado
	// por eso se usa el *
	if( *pNum2 !=0){
		 *pResultado= *pNum1 / (float) * pNum2;

	}else{
		printf (" No se puede dividir por cero \n");
	}

	//NOTE QUE NO HAY VALOR DE RETORNO PORQUE TODO SE LLEVO A CABO CON APUNTADORES
}