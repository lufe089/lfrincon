#include <stdio.h>
#include <stdlib.h>
#include <stdexcept>
  

typedef enum opc_validacion{
 	POSITIVO, PAR, NO_ZERO
}opc_validacion_e;


typedef enum operaciones{
 	SUMA, DIVISION, GUARDAR
}operaciones_e;

FILE* abrirArchivo(const char * path, const char * modo) {
	if (path != NULL) {
		FILE* pFile = fopen(path, modo);
		if (pFile == NULL){
			throw std::logic_error ("No se pudo abrir correctamente el archivo \n");
		}
		return pFile;
	}
	else{
		throw std::logic_error ("No se recibio la ruta del archivo \n");
	}	
}

void validarNumerosErrorLogico(int num, opc_validacion_e opcValidacion){
  
  switch (opcValidacion){
  	case POSITIVO: 
	    if (num < 0){
    		throw std::logic_error ("El número debe ser positivo \n");
  	    }
  	    break;
  	case PAR: 
  		if (num %2 != 0){
    		throw std::logic_error ("Solo se operan numeros pares \n");
  	    }
		break;	
		
	case NO_ZERO:
		if (num == 0){
    		throw std::logic_error ("No se pueden hacer divisiones por cero \n");
  	    }
		break;	
  }
  
}


void pedirNumerosCalc(int * num1, int * num2){

    // Se llaman las validaciones para el primer número
	printf("Introduzca el primer numero:\n");
	scanf("%d", num1);
	validarNumerosErrorLogico(*num1, POSITIVO);
	validarNumerosErrorLogico(*num1, PAR);
	
	printf("Introduzca el segundo numero:\n");
	scanf("%d", num2);
	validarNumerosErrorLogico(*num2, POSITIVO);
	validarNumerosErrorLogico(*num2, PAR);
} 
	
int sumar(int num1, int num2){
	int suma = num1 + num2;
	printf("La suma es %d \n", suma);
	return suma;
}

float dividir(int num1, int num2){
	
	validarNumerosErrorLogico(num2, NO_ZERO);
	float division = (float)num1 /num2;
	printf("El resultado de la division es %f \n", division);
	return division;
}

void guardarArchivoFPrint(FILE* pFile, int sumaResul, float divisionResult) {
	fprintf(pFile, "suma: %d\t division: %f\n", sumaResul,divisionResult);
}



int main()
{
   int num1;
   int num2;
   int errores = 0;
   int opc = 0;
   int sumaResult = 0;
   float divisionResult = 0;
	
   printf("Bienvenido al programa \n");
   
   // Se piden las validaciones de los datos
   do{
	   try{
	  	 pedirNumerosCalc(&num1, &num2);
	  	 errores = 0;
	   }catch(std::logic_error &e){
	   	 printf("Este programa tiene el siguiente error de validacion:  %s", e.what());
	   	 errores = 1;
	   }
    } while (errores == 1);
    
    do{
	
		try{
	    	printf(" Ahora digame que operacion quiere: \n 0. Sumar \n 1. Dividir \n 2. Guardar \n , -1. Salir \n");
	    	scanf("%d", &opc);
	    	switch(opc){
				case SUMA:      sumaResult= sumar(num1,num2);
					            break; 
				case DIVISION:  divisionResult= dividir(num1,num2);		   
					   			break; 
				case GUARDAR:   //Aqui va a morir para que funcione ponga un nombre de un archivo en lugar del NULL
								FILE * pArchivo = abrirArchivo(NULL, "a");
							    guardarArchivoFPrint(pArchivo, sumaResult, divisionResult);
								break;
		
			}
		}
		catch(std::logic_error &e){
			 printf("Este programa tiene el siguiente error de validacion:  %s", e.what());
		}
	}
	while (opc !=-1);
 
}
