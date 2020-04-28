
#include "OrdenamientoRecursivo.h"

/* Esta función sirve para facilitar el seguimiento del codigo */
void imprimirRango(int arreglo[], int desde, int hasta) {

	int i = 0;
	for (i = desde; i <= hasta; i++) {
		printf("Posicion: %d -- Valor: %d \n", i, arreglo[i]);
	}
}
void intercambiar(int arreglo[], int posicion1, int posicion2) {
	int tmp;
	tmp = arreglo[posicion2];
	arreglo[posicion2] = arreglo[posicion1];
	arreglo[posicion1] = tmp;
}


/* Función que entrega la posición del pivote, tomando como pivote inicial el elemento del final de la lista */
int partirYOrdenarPivoteInicial(int arreglo[], int posPrimerElem,
		int posUltimoElem) {
	int valorPivote = arreglo[posPrimerElem]; // Valor del pivote
	int posIzquierda = posPrimerElem + 1; // Se incrementa uno  pq el primer elemento será el pivote
	int posDerecha = posUltimoElem;
	printf(
			"..PARTIR_ORDENAR:\n valorPivote:%d, posPivote:%d, posizquierda(posPivote+1):%d, posDerecha: %d\n",
			valorPivote, posPrimerElem, posIzquierda, posDerecha);
	imprimirRango(arreglo, posIzquierda, posUltimoElem);
	//Se mueven elementos mientras que no se crucen los indices
	do {
		while (posIzquierda <= posDerecha
				&& arreglo[posIzquierda] <= valorPivote) {
			//Los elementos estan en el lado correcto, no hay que intercambiar.
			//Se avanza para encontrar elemento a intercambiar
			posIzquierda++;
			printf("PARTIR_ORDENAR_Aumento posIzq %d \n", posIzquierda);
		}
		while (posIzquierda <= posDerecha && arreglo[posDerecha] > valorPivote) {
			//Los elementos estan en el lado correcto, no hay que intercambiar.
			//Se avanza para encontrar elemento a intercambiar
			posDerecha--;
			printf("PARTIR_ORDENAR_Disminuyo posDer %d \n", posDerecha);
		}
		//Se encontraron elementos en posiciones que deben intercambiarse
		if (posIzquierda < posDerecha) {
			printf(
					"PARTIR_ORDENAR_ Intercambiar: Valor pivote:%d posIzq:%d - valor:%d , posDer:%d -valor: %d \n",
					valorPivote, posIzquierda,arreglo[posIzquierda], posDerecha,
					arreglo[posDerecha]);
			intercambiar(arreglo, posIzquierda, posDerecha);
			posIzquierda++;
			posDerecha--;
			printf("PARTIR_ORDENAR_Arreglo despues de intercambio:___\n");
			imprimirRango(arreglo, posPrimerElem, posUltimoElem);

		}
	} while (posIzquierda <= posDerecha);
	printf(" PARTIR_ORDENAR_Fin while externo INDICES posIzquierda:%d  ,posDerecha:%d  \n",
			posIzquierda, posDerecha);
	//intercambiar pivote
	if (arreglo[posDerecha] != valorPivote) {
		printf(
				"PARTIR_ORDENAR_INTERCAMBIO PIVOTE: valorPivote:%d en posicion:%d, con posicion: %d, valor %d \n",
				valorPivote, posPrimerElem,  posDerecha,arreglo[posDerecha]);
		intercambiar(arreglo, posPrimerElem, posDerecha);

	}
	printf("PARTIR_ORDENAR_Despues de Intercambiar pivote \n");
	imprimirRango(arreglo, posPrimerElem, posUltimoElem);
	//Retorna la posicion del pivote
	return posDerecha;
}

/* Función que implementa ordenamiento por quicksort. */
void quickSort(int arreglo[], int posIzquierda, int posDerecha) {
	//Posición del pivote
	int posPivote;
	printf("\n\nPrincipal_QUICKSORT: posIzquierda:%d, posDerecha:%d\n", posIzquierda,
			posDerecha);
	if (posIzquierda < posDerecha) {
		//Ordenar elementos para un pivote
		posPivote = partirYOrdenarPivoteInicial(arreglo, posIzquierda,
				posDerecha);
		printf("Principal_Posicion pivote:%d \n", posPivote);
		//Repetir el proceso con los arreglos resultantes
		printf("\nPrincipal_Nueva invocacion quick sort desde %d hasta posIzquierda %d\n",
				posIzquierda, posPivote - 1);
		quickSort(arreglo, posIzquierda, posPivote - 1);
		printf("\nPrincipal_Nueva invocacion desde %d hasta posDerecha %d\n",
				posPivote + 1, posDerecha);
		quickSort(arreglo, posPivote + 1, posDerecha);
	}
}


/* Funcion que se encarga de mezclar en un arreglo los valores desde la posición inicial hasta la posición final, en orden ascendente */
void merge(int arreglo[], int posInicial, int posMitad, int posFinal) {
	int tamArrayTemp = (posFinal - posInicial)+1;
	int arregloParcial[tamArrayTemp];
	int indexMitadUno = posInicial;
	int indexMitadDos = posMitad + 1;
	int indexArregloParcial = 0;
	int indexArregloFinal;
	printf("\n Inicia mezcla posInicial:%d, posMitad:%d, posFinal:%d\n ",
			posInicial, posMitad, posFinal);
	printf(" Arreglo para mezclar:____\n");
	imprimirRango(arreglo, posInicial,posFinal);
	while (indexMitadUno <= posMitad && indexMitadDos <= posFinal) {
		//Se hacen las comparaciones para el ordenamiento
		if (arreglo[indexMitadUno] <= arreglo[indexMitadDos]) {
			//Se pone primero en el arreglo parcial el contenido de indexMitadUno
			arregloParcial[indexArregloParcial] = arreglo[indexMitadUno];
			//Se incrementa el index de mitad dos para avanzar en el arreglo
			indexMitadUno++;
		} else {
			//Se pone primero en el arreglo parcial el contenido de indexMitadDos
			arregloParcial[indexArregloParcial] = arreglo[indexMitadDos];
			//Se incrementa el index de mitad dos para avanzar en el arreglo
			indexMitadDos++;
		}
		//Se incrementa el indice del arreglo parcial
		indexArregloParcial++;
	}
	//Se acomodan los elementos que faltan
	while (indexMitadUno <= posMitad) {
		arregloParcial[indexArregloParcial] = arreglo[indexMitadUno];
		indexArregloParcial++;
		indexMitadUno++;
	}
	while (indexMitadDos <= posFinal) {
		arregloParcial[indexArregloParcial] = arreglo[indexMitadDos];
		indexArregloParcial++;
		indexMitadDos++;
	}
	//Se actualizan los valores en el arreglo de entrada
	printf("Arreglo temporal mezcla:____\n");
	imprimirRango(arregloParcial, 0,indexArregloParcial-1);
	
	for (indexArregloParcial = 0; indexArregloParcial < tamArrayTemp;
			indexArregloParcial++) {
		indexArregloFinal = posInicial + indexArregloParcial;
		arreglo[indexArregloFinal] = arregloParcial[indexArregloParcial];
	}
	printf("Arreglo ajustado \n");
	imprimirRango(arreglo, posInicial, posFinal);

}
/* Funcion que ordena usando el algoritmo de ordenamento merge sort */
void mergeSort(int arreglo[], int posInicial, int posFinal) {

	//Condicion de salida recursion
	//Cuando no se cumple, esto indica que se ha llegado a arrays de un elemento
	printf("\n posInicial:%d, posFinal:%d, subArray a ordenar: \n", posInicial,
			posFinal);
	imprimirRango(arreglo, posInicial, posFinal);
	if (posInicial < posFinal) {
		int posMitad = (posInicial + posFinal) / 2;
		//Se parte el arreglo recursivamente
		//Primera mitad ( en la primera iteracion de la 0 a la posMitad)
		mergeSort(arreglo, posInicial, posMitad);
		//Segunda mitad ( en la primera iteracion de la posMitad+1 a posFinal)
		mergeSort(arreglo, posMitad + 1, posFinal);
		//Mezclar arreglo ( En este procedimiento se ordena el arreglo)
		merge(arreglo, posInicial, posMitad, posFinal);
	}else{
		printf(".....Para la recursion\n");
	}

}


void imprimirAscendente(int arreglo[], int size) {

	int i = 0;
	for (i = 0; i < size; i++) {
		printf("Posicion: %d -- Valor: %d \n", i, arreglo[i]);
	}
}

