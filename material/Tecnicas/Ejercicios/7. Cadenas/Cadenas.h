#include <stdio.h>
//Se incluye para los ejemplos de strcpy y strcat
#include <string.h>
#define SIZE 80


/*EJEMPLOS*/
/* Lee caracteres con getchar y los imprime con putchar */
void leerEscribirCadenaGetPutChar();

/* Lee una cadena que con scanf y la imprime con printf. La cadena
queda guardada en el parámetro de entrada que es un paso por referencia*/
void leerEscribirCadenaScanfPrintf(char arregloCaracteres[]);

/* Lee una cadena que con fgets y la imprime con puts. La cadena
queda guardada en el parámetro de entrada que es un paso por referencia*/
void leerEscribirCadenaFgetsPuts(char arregloCaracteres[] );

/* Muestra el funcionamiento de strcpy 
Añade una cadena a otra. La cadena destino debe tener espacio suficiente para
soportar la cadena que se le quiere concatenar
*/
void usarStrcpy();

/* Muestra el funcionamiento de strncat
Copia los caracteres de la cadena fuente a la cadena destino
*/
void usarStrcpy();

/* Limpia el bufer de entrada para evitar problemas
cuando se leen cadenas*/
void flush_in(); 

/* Muestra el funcionamiento de strcat */

/*EJERCICIOS A COMPLETAR */

/* Cuenta cuantos elementos tiene una cadena desde la primera
posicion hasta que encuentra el caracter de fin de cadena '\0'*/
int calcularLongitudCadena(char arregloCaracteres[] );

/* Cuenta de un arreglo de caracteres cuantos digitos tiene, cuantos caracteres alfanumericos
tiene y cuántos caracteres especiales tienen. Usar solo los valores de ASCII 
para hacer las cálculos. Aprovechar la operación calcularLongitudCadena */
void contarTipoLetras(char arregloCaracteres[] );

/* Lee caracteres con getchar. Aumenta el contador cuando la letra es una a
minúscula o mayúscula. Lee las letras hasta que el usuario ingresa un punto.
Al terminar retorna la cantidad de veces que estaba la letra. Aprovechar la operación calcularLongitudCadena 
*/
int contarLetraA( );

/* Sin usar funciones de la biblioteca de string pase los caracteres del arreglo
a mayusculas. Si la letra es minuscula para pasarla a mayuscula simplemente se debe
restar a su valor entero 32 elementos. Aproveche la operación calcularLongitudCadena  */
void pasarMayusculas(char arregloCaracteres[] );

/*Una operación que puede ser útil es la de invertir una cadena. 
Usted debe implementar una operación que reciba una cadena cadena de máximo 50 caracteres con cualquier tipo de caracteres. 
Esta operación debe crear 3 arreglos a partir del original. 
El primer arreglo contiene los caracteres numéricos de la frase ingresada. 
El segundo tendrá las letras en mayúscula. 
El tercero las letras en minúscula. 
El cuarto arreglo contiene todos los demás símbolos. 
La restricción para cada array es que debe acomodarse en orden inverso al 
que aparece en la frase. 
Para finalizar debe mostrar el contenido de cada arreglo en una línea 
diferente cada uno. Tenga cuidado en recorrer la cadena únicamente hasta 
que encuentre el carácter de terminación. */
void separarCadenas (char arregloCaracteres[]);

