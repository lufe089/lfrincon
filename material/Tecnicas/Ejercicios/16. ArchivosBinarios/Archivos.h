#ifndef ARCHIVOS_H_
#define ARCHIVOS_H_


#include <stdlib.h>
#include <stdio.h>

typedef struct {
	char nombre_empleado[25];
	int edad;
	float salario;
} empleado_t;


FILE* abrirArchivo(char path[], char modo[]);
void guardarEnteroArchivoBinario(FILE *pFile);
void leerEnteroArchivoBinario(FILE *pFile); 
void guardarArregloEnterosArchivoBinario(FILE *pFile, int tamArreglo);
void leerArregloEnterosArchivoBinario(FILE *pFile, int tamArreglo);
void leerArregloEmpleadosBinario(FILE* pFile, int);
void guardarArregloEmpleadosBinario(FILE* pFile, int);
void leerEmpleadosUnoaUnoBinario(FILE* pFile);

#endif /* ARCHIVOS_H_ */