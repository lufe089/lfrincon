#include "Recursion.h"

int ejemploFactorial(int num){
    if (num == 0){
        return 1;
    }
    else{
        return num * ejemploFactorial(num-1);
    }
}

/* Imprime cuenta regresiva de n a cero, al llegar a cero dice boom 
 	Solo imprime y llama*/
void imprimirCuentaRegresiva(int n){
	if (n == 0){
		printf("Boom \n"); // No depende de la recusión
	} else {
		printf("%d ",n); // Imprimo que es lo que me pide el programa
		imprimirCuentaRegresiva(n-1);
	}

}
/* Operacion recursiva que cuenta cosas
 no imprime, lleva la cuenta por lo que a diferencia de los anteriores necesito retornar cosas 
 en todos los flujos*/

int contarMultiplos3 (int n){
	if (n == 3){ // Caso base no depende de la recursion, es el numero mas pequeño
		return 1;
	} else {
		if (n % 3 == 0) {
			return  1 + contarMultiplos3(n-1);
		} else {
			// El cero no sería necesario, es solo a manera de ejemplo
			return 0 + contarMultiplos3(n-1);
		}
	}
}

/* Suma de los numeros multiplos del 3. A diferencia del anterior
no cuenta (1 / 0) sino que lleva un acumulado */

int sumarMultiplos3 (int n){
	if (n == 3){ // Caso base no depende de la recursion
		return n;
	} else {
		if (n % 3 == 0) {
			return  n + sumarMultiplos3(n-1);
		} else {
			// El cero no sería necesario, es solo a manera de ejemplo
			return 0 + sumarMultiplos3(n-1);
		}
	}
}


// Haga: Ejercicio contador de los números que on multiplos de 3 y de 5 al mismo tiempo
// Haga: suma de todos los números del 0 hasta x número.

/* Recursión cuando necesita mandar información entre iteraciones.
Mayor de un arreglo, por facilidad se hace decremental */
/* Reviso que todos los caminos tengan el return, se este
disminuyendo el problema para hacerlo mas pequeño y se 
este haciendo la logica que necesito */
int buscarMayor (int * arreglo, int n, int pos, int mayorTemp){

	if (pos == 0){
		// Ya recorri todo, entonces retorno el mayor que tenga
		return mayorTemp;
	} else {
		// Busco el mayor
		if (arreglo[pos] > mayorTemp ){
			// LLamo la funciona recursiva para verificar si el nuevo mayor
			// que encontré seguiría siendo el mayor
			return buscarMayor(arreglo, n, pos-1, arreglo[pos]);
		} else {
			//Llamo a la funcion recursiva pero sin cambiar el mayor que ya tengo
			return buscarMayor( arreglo, n, pos-1, mayorTemp);
		}

	}

}


/* Sumar los numeros entre dos intervalos */
int sumarNumerosEntreIntervalos(int lInfInt, int lSupInt){
	if (lInfInt == lSupInt){
		return 0; // No se acumula nada en la suma
	} else {
		return lSupInt + sumarNumerosEntreIntervalos (lInfInt,lSupInt-1);
	}
}

/* Modifique la suma entre intervalos para que cuente cuantas veces se hacen llamados 
recursivos */
int sumarNumerosEntreIntervalosCuenta(int lInfInt, int lSupInt, int cuenta){
	printf("LLamado recursivo # %d \n", cuenta++);
	if (lInfInt == lSupInt){
		printf("Alcance condición de parada \n");
		return 0; // No se acumula nada en la suma
	} else {
		return lSupInt + sumarNumerosEntreIntervalosCuenta (lInfInt,lSupInt-1, cuenta);
	}
}


/* Operacion recursiva que acumula entre llamados */


/* Operacion recursiva que tiene condicionales y paso de parametros entre
operaciones, por ejemplo para hallar el mayor */
