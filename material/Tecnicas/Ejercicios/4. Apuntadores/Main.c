#include "Apuntadores.h"

int main(){

	int variableUno= 50;
	int variableDos= 11;
	float division=0.0;

	//Se incluye el & en la invocación de la función para obtener las direcciones de memoria
	dividir(&variableUno, &variableDos, &division);

	//Se prueba el resultado. Con .2f se establece que el numero decimal se mostrará con dos cifras
	printf(" El valor de la division es %.2f \n", division);

	//Incluir aqui el esto de las operaciones desarrolladas para probar que funcionan. 

}