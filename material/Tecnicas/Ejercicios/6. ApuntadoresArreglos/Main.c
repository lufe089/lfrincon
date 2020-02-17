#include "Arreglos.h"

int main()
{

	int tamUno=15, tamDos=5, tamDiferencia=0;
	int arregloUno[tamUno], arregloDos[tamDos];
	int arregloDiferencia[tamUno];
	//Se llena el arregloUno
	llenarArreglo(arregloUno, tamUno, 2);
	//Se imprime en pantalla el arregloUno
	imprimirArregloAritmeticaPunteros(arregloUno, tamUno);
	//Se llena el arregloDos
	llenarArreglo(arregloDos, tamDos, 5);
	// Se calcula la diferencia del arregloUno y el arregloDos
	calcularDiferenciaArreglos(arregloUno,arregloDos,arregloDiferencia, tamUno,tamDos, &tamDiferencia);
	// Se imprime el arregloDiferencia. Note que se imprime hasta tamDiferencia que es el tamaño real del arregloDiferencia
	imprimirArregloAritmeticaPunteros(arregloDiferencia, tamDiferencia);

	//Completar con las otras operaciones. Reutilice la funcion imprimir para ver los resultados.
	// Puede llenar el arreglo con otros valores si le conviene para sus pruebas. Note que la
	// operacion llenarArreglo llena el arreglo con números consecutivos que inician en el valor
	// que se recibe como último parámetro

	
	return 0;
}
