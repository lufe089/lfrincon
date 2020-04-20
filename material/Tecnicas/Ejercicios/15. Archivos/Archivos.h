#include <stdlib.h>
#include <stdio.h>

typedef struct {
	char nombre_empleado[25];
	int edad;
	float salario;
} empleado_t;


FILE* abrirArchivo(char path[], char modo[]);
void leerArchivoFScanf(FILE* pFile);
void guardarArchivoFPrint(FILE* pFile, int numEmpleados);