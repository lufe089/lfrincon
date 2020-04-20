#include "Archivos.h"

FILE* abrirArchivo(char path[], char modo[]) {
	if (path != NULL) {
		FILE* pFile = fopen(path, modo);
		return pFile;
	}
	return NULL;
}


void guardarEnteroArchivoBinario(FILE *pFile) {
	int varEntera = 7;
	//varEntera: espacio de memoria
	//sizeof(int): tamaño en bytes de un entero
	//1 un solo entero
	//en el archivo
	fwrite(&varEntera, sizeof(int), 1, pFile);
	fclose(pFile);
}

void leerEnteroArchivoBinario(FILE *pFile) {
	int varEntera;
	//varEntera: espacio de memoria
	//sizeof(int): tamaño en bytes de un entero
	//1 un solo entero
	//en el archivo
	fread(&varEntera, sizeof(int), 1, pFile);
	fclose(pFile);
	printf("El valor de la variable del archivo es %d\n", varEntera);
}

void imprimirArreglo(int arreglo[], int tamArreglo){
	printf(" Arreglo a guardar \n");
	int i=0;
	for(i=0; i<tamArreglo; i++){
		printf(",%d ", arreglo[i]);
	}
	printf("\n");
}

void guardarArregloEnterosArchivoBinario(FILE *pFile, int tamArreglo) {
	int arregloEntero[tamArreglo], i;
	for (i = 0; i < tamArreglo; i++) {
		arregloEntero[i] = i + 1;
	}

	imprimirArreglo(arregloEntero,tamArreglo);
	fwrite(arregloEntero, sizeof(int), tamArreglo, pFile);
	fclose(pFile);
}

void leerArregloEnterosArchivoBinario(FILE *pFile, int tamArreglo) {
	int arregloEntero[tamArreglo], i;
	fread(arregloEntero, sizeof(int), tamArreglo, pFile);
	fclose(pFile);
	printf("Leyendo arreglo de archivo \n");
	for (i = 0; i < tamArreglo; i++) {
		printf("Arreglo en posicion %d con valor %d\n", i, arregloEntero[i]);

	}
}


void guardarArregloEmpleadosBinario(FILE* pFile, int numEmplead) {

	empleado_t * pArregloEmpleados= (empleado_t*) calloc(sizeof(empleado_t),numEmplead);
	int i;
	for(i=0; i<numEmplead; i++){
		printf("Ingrese un nombre:\n ");
		scanf("%s", pArregloEmpleados[i].nombre_empleado);
		printf("Ingrese la edad:\n ");
		scanf("%d", &pArregloEmpleados[i].edad);
		printf("Ingrese el salario:\n ");
		scanf("%f", &pArregloEmpleados[i].salario);
	}

	//Se escribe el archivo
	fwrite(pArregloEmpleados, sizeof(empleado_t), numEmplead, pFile);
	fclose(pFile);
	//Se libera la memoria del arreglo
	free(pArregloEmpleados);
}

/* Esta función lee empleados hasta que se acabe el archivo*/
void leerArregloEmpleadosBinario(FILE* pFile, int numEmplead) {
	//Se reserva la memoria donde quedaran los datos leidos del archivo
	empleado_t * pArregloEmpleados= (empleado_t*) calloc(sizeof(empleado_t),numEmplead);
	fread(pArregloEmpleados, sizeof(empleado_t), numEmplead, pFile);
	int i;
	//Se imprimen los datos para probar que fueron leidos correctamente
	for(i=0; i<numEmplead; i++){
		printf(
					"\nValores leidos archivo binarios: nombre: "
					"%s, Edad: %d, Salario:%6.0f\n",
					pArregloEmpleados[i].nombre_empleado, pArregloEmpleados[i].edad, pArregloEmpleados[i].salario);

	}

	fclose(pFile);
	//Se libera la memoria del arreglo
	free(pArregloEmpleados);
}

void leerEmpleadosUnoaUnoBinario(FILE* pFile) {
	empleado_t  empleado;
	while(!feof(pFile)){
		fread(&empleado, sizeof(empleado_t), 1, pFile);
		printf(
					"\nValores leidos archivo binarios: nombre: "
					"%s, Edad: %d, Salario:%6.0f\n",
					empleado.nombre_empleado, empleado.edad, empleado.salario);

	}
	fclose(pFile);
}
