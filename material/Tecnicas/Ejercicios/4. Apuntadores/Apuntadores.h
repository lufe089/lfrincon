#include <stdio.h>
#include <stdlib.h>

/* OPERACION DE EJEMPLO */
void dividir (int* pNum1, int* pNum2, float *pResultado);


/* Recibe un apuntado a un numero entero, lo eleva al cuadrado 
multiplicandolo el contenido por si mismo.  Al salir el contenido 
debe estar cambiado */
void elevarCuadrado(int * pValor);

/* Recibe dos variables enteras, las suma y guarda el resulado en el contenido
del apuntador pResultado */
void sumarNumeros(int num1, int num2, int * pResultado);

/* Recibe dos apuntadores a variables enteras, suma su contenido y guarda el resulado en el contenido
del apuntador pResultado */
void sumarNumerosApuntadores(int* pNum1, int* pNum2, int *pResultado);

/* Recibe dos apuntadores a variables enteras. Al salir de esta operación, el valor al que apunta
cada apuntador debe estar intercambiado . Por ejemplo si el primer apuntador apunta a la variable x 
que vale 1 y el segundo apunta a la variable y que vale 3, al salir de esta operación
la varible y debe valer 1 y la variable x debe valer 3*/ 
void intercambiar ( int *pValor1, int *pValor2);