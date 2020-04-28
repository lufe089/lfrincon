/*
 * OrdenamientoArreglos.h
 *
 *  Created on: 13/03/2014
 *      Author: LuFe
 */

#ifndef ORDENAMIENTOARREGLOS_H_
#define ORDENAMIENTOARREGLOS_H_
#include <stdio.h>
#define TAM_ARREGLO 5

void imprimirAscendente(int arreglo[],int size);
void quickSort(int arreglo[], int izquierda, int derecha);
void mergeSort(int arreglo[], int posInicial, int posFinal);
void ordernarA(int arreglo[], int size);
void ordernarB(int arreglo[], int size);
#endif /* ORDENAMIENTOARREGLOS_H_ */
