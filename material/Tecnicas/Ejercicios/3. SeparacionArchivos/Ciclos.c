#include "Ciclos.h"


///Ejemplos con while

/* Suma los números impares del 1 al 100 e imprime la cantidad 
 * de sumas realizadas*/
 void sumarImparesCiclo(){
	int numActual=1, suma=0, contSumas=0;
	while(numActual<=100){
		suma += numActual;
		numActual+=2;
		contSumas++;
	}
	printf("El número de sumas realizadas fue  %d ", contSumas);  
}

/* Suma los números impares del 1 al 100 e imprime la cantidad 
 * de sumas realizadas*/
void sumarImparesCicloV2() {
	int numActual=1, suma=0, contSumas=0;
	while(numActual<=100) {
		if(numActual%2!=0) {
			suma += numActual;
			contSumas++;
		}
		numActual++;
	}
	printf("El número de sumas realizadas fue  %d ", contSumas);
}


void ejemploWhile() {
	int potencia=2;
	int contador=0;
	while(potencia <= POTENCIAMAX) {
		potencia *= 2;
		contador++;
	}
	printf("La primera potencia de 2 superior"
	       "a 1000 es %d se tuvo que elevar el 2 %d veces\n", potencia, contador);
}

void sumarNumerosPorConsola(){
	int suma=0, num=0;
	while(num!=-1){
		printf("Ingrese un número");
		scanf("%d", &num);
		if(num!=-1){
			suma+=num;
		}
	}
	printf("El valor de la suma es %d", suma);
}

void sumarWhile() {
	int suma=0, contador=1;
	while(contador<=10) {
		suma+=contador;
		contador++;
	}
	printf("El valor de la suma es %d\n", suma);
}

/* Ejemplos con doWhile */

void sumarNumerosDoWhile(){
	int suma=0, num;
	do{
		printf("Ingrese un número");
		scanf("%d", &num);
		if(num!=-1){
			suma+=num;
		}
	}while(num!=-1);
	printf("El valor de la suma es %d", suma);
}

void sumarDoWhile() {
	int suma=0, in=0;
	do {
		suma+=in;
		printf("Ingrese un numero. -1 para terminar");
		scanf("%d",&in);

	} while(in!=-1);
	printf ("El valor de la suma es %d", suma);
}

/* Ejemplos con FOR */

void ejemploConBreak() {
	int i=0;
	int suma=0;
	for(i=0; i<100; i++ ) {
		/* Sumar los numeros del 1 al 100 hasta
		 * que la suma sea superior a 10 */
		if(suma > 10) {
			break;
		}

		suma+=i;
	}
	printf("El valor de la suma con break es : %d \n",suma);
}

void ejemploSinBreak() {
	int i=0;
	int suma=0;
	for(i=0; i<100; i++ ) {
		/* Sumar los numeros del 1 al 100 */
		suma+=i;
	}
	printf("El valor de la suma sin break es : %d \n",suma);
}
void ejemploConContinue() {
	int i=0;
	int suma=0;
	for(i=0; i<10; i++ ) {
		/*Sumar los numeros del 1 al 10 con excepcion del 8*/
		if(i == 8) {
			continue;
		}
		suma+=i;
	}
	printf("El valor de la suma con continue es : %d \n",suma);
}

void sumarNumerosFor() {
	int i=0;
	int suma=0;
	for(i=0; i<10; i++ ) {
		/*Sumar los numeros del 1 al 10 */
		suma+=i;
	}
	printf("El valor de la suma es : %d \n",suma);
}

void ejemploNoBreak() {
	int i=0;
	for(i=0; i<10; i++ ) {
		if(i==5) {
			break;
		}
		printf("El valor del numero es : %d \n",i);
	}
}

void forMultipleAsignacion() {
	int i,adicional;
	for(i=10, adicional=15; i>1 && adicional>20; i--, adicional++) {
		printf("Numero consecutivo\n %d", i);
	}
}

