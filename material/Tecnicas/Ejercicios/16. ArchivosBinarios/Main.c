
#include "Archivos.h"


void probarBinarioBasico(){
	char path[] = "archivoBinarioBasico";
    char modo[] = "w";
    FILE* pFile = abrirArchivo(path, modo);
    if(pFile != NULL) {
		printf("Guardando archivo binario, solo un numero\n");
		guardarEnteroArchivoBinario(pFile);
	}else {
			printf("No se pudo abrir correctamente el archivo\n");
	}
	printf("Leyendo archivo binario de un solo numero\n");
	pFile = abrirArchivo(path, "r");
	if(pFile != NULL) {
		leerEnteroArchivoBinario(pFile);
		fclose(pFile);
	} else {
		printf("No se pudo abrir correctamente el archivo\n");
	}
}


void probarArregloEnteros (){
	char path[] = "archivoBinarioArregloEnteros";
    char modo[] = "w";
    FILE* pFile = abrirArchivo(path, modo);
	if(pFile != NULL) {
		printf("Guardando archivo binario arreglo de numeros\n");
		guardarArregloEnterosArchivoBinario(pFile, 10);
	}else{
		printf("No se pudo abrir correctamente el archivo\n");
	}
	
	pFile = abrirArchivo(path, "r");
	if(pFile != NULL) {
			printf("Leyendo archivo binario de arreglo de numeros\n");
			leerArregloEnterosArchivoBinario(pFile, 10);
	} else {
		printf("No se pudo abrir correctamente el archivo\n");
	}
}

void probarStruct (){
	char path[] = "archivoBinarioEmpleado";
    char modo[] = "a";
    FILE* pFile = abrirArchivo(path, modo);
	if(pFile != NULL) {
		guardarArregloEmpleadosBinario(pFile,2);
	}else{
		printf("No se pudo abrir correctamente el archivo\n");
	}
	
	pFile = abrirArchivo(path, "r");
	if(pFile != NULL) {
		printf("Leyendo archivo binario de empleados\n");
		leerArregloEmpleadosBinario(pFile,2);
	} else {
		printf("No se pudo abrir correctamente el archivo\n");
	}
	
	printf("Probar leer uno a uno \n");
	pFile = abrirArchivo(path, "r");
	if(pFile != NULL) {
			printf("Leyendo archivo binario de empleados\n");
			leerEmpleadosUnoaUnoBinario(pFile);
	} else {
		printf("No se pudo abrir correctamente el archivo\n");
	}
}

int main()
{
   probarBinarioBasico();
   probarArregloEnteros();
   probarStruct();
    return 0;
}
