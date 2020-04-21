#include <stdlib.h>
#include <stdio.h>

typedef struct {
	char nombre_empleado[25];
	int edad;
	float salario;
} empleado_t;

typedef enum Opcion{
	GUARDAR, LEERSCANF, LEERFGETS
}opc_e;

FILE* abrirArchivo(char path[], char modo[]);
void leerArchivoFScanf(FILE* pFile);
void guardarArchivoFPrint(FILE* pFile, int numEmpleados);


// Para completar

void guardarFPuts(FILE * pFile);

void leerConFGets(FILE* pFile);

void leerConFGetc(FILE* pFile);

void contarNumLineas(FILE* pFile);

/* Recibe la ruta del archivo, la cantidad de numeros aleatorios enteros que va a generar. 
Como resultado. En su disco deben quedar guardados un archivo de números aleatorios ( un número por cada línea)..
Tenga encuenta que en su archivo debe quedar guardada de alguna manera la cantidad de números aleatorios que
componen el archivo*/
void generarArchivoNumerosAleatorios();

// void generarArchivoNumerosAleatorios(Completar);

/* Lee el archivo creado con la función anterior. Este archivo tiene (como usted lo hubiera definido) por cada línea un número aleatorio.
Como resultado en memoria en un arreglo deben quedar cargados los números aleatorios del archivo */ 
// void leerArchivoNumerosAleatorios(Completar)