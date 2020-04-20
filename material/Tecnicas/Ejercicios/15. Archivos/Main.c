
#include "Archivos.h"

int main()
{
	//Cambiar el path
	char path[] = "empleadosText.txt";
	char modo[] = "a";
	FILE* pFile = abrirArchivo(path, modo);
	if(pFile!=NULL){
		printf("Guardando archivo");
		guardarArchivoFPrint(pFile, 2);
		printf("Leyendo archivo");
		fclose(pFile);
		pFile = abrirArchivo(path, "r");
		leerArchivoFScanf(pFile);
	}
	else{
		printf("No se pudo abrir correctamente el archivo");
	}
	return 0;
}



