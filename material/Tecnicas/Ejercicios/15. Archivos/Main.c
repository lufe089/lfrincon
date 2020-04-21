
#include "Archivos.h"


void guardarEmpleados(char path[]) {
	char modo[] = "a";
	FILE* pFile = abrirArchivo(path, modo);
	int numEmpleados = 2;
	if(pFile!=NULL){
		printf("Guardando archivo empleados \n");
		guardarArchivoFPrint(pFile, numEmpleados);
		fclose(pFile);
	}
}

void leerEmpleados(char path[]){
	FILE* pFile = abrirArchivo(path, "r");
	if(pFile!=NULL){
		printf("Leyendo archivo");
		leerArchivoFScanf(pFile);
		fclose(pFile);
	}
}

int menu(){
	int opc = 0; 
	//Cambiar el path
	char path[] = "empleadosText.txt";
	do{
		printf("1. Guardar archivo de empleados \n");
		printf("2. Leer archivo de empleados con scanf \n");
		printf("3. Leer archivo con Getc \n");
		printf("-1. Salir \n");
		scanf("%d",&opc);

		// Aqui hay un error... de lógica... ¿Cuál será?
		switch(opc) {
			case GUARDAR: guardarEmpleados(path);
						  break;

			case LEERSCANF: leerEmpleados(path);
							break;

			case LEERFGETS: printf("A completar ..");

		}				
	}while (opc != -1);
	return opc;
}

int main()
{
	menu();
	return 0;
}



