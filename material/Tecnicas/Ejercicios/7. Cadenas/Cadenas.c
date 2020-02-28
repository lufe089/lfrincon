#include "Cadenas.h"


void leerEscribirCadenaGetPutChar(){
	printf(" Usando getChar y putChar, termina con ctrl +z si es windows \n");
	int c=0;
	do{
		//Se lee el caracter y se guarda su valor entero
		c=getchar();
		//Se imprime el caracter
		putchar(c);
	}while( c!= EOF); // EOF indica caracter de fin, se puede cambiar por otro caracter que termine el ciclo
}

void leerEscribirCadenaScanfPrintf(char arregloCaracteres[]){

	int tamMax=SIZE -1;
	printf(" \nEscribir leer scanf - printf \n");
	printf("Ingrese una cadena  \n");
	//Se define el tamanio maximo
	scanf("%79s", arregloCaracteres);
	printf("Imprimir con printf %s \n", arregloCaracteres);
	/* Cuando se leen datos con scanf y se desea continuar 
	leyendo cadenas es necesario limpiar el buffer se llama
	a la función local*/
	flush_in();

}

void leerEscribirCadenaFgetsPuts(char arregloCaracteres[]){
	printf(" \n Escribir leer fgets puts \n");
	printf("Leer con fgets Ingrese una cadena  \n");
	fgets(arregloCaracteres,SIZE,stdin);
	//Limpiar el buffer
	//flush_in();
	printf("Imprimir con puts la cadena  \n");
	puts(arregloCaracteres);
}

void usarStrcpy(){

	char texto1[]="corta";
	char textoDos[]="larguisima";
	
	//Sin son arreglos estáticos debo saber el tamaño
	char copiaTextoUno[20];
	//Sin son arreglos estáticos debo saber el tamaño
	char copiaTextoDos[20];
	 
	 printf("\n Ejemplo strcpy \n");

	 strcpy(texto1,copiaTextoUno);
	 
	 //Se imprime texto la primera copia
	 printf("Copia texto uno %s\n",copiaTextoUno);
	 
	 strcpy(textoDos,copiaTextoDos);
	  
	  //Se imprime texto la segunda copia
	 printf("Copia texto dos %s\n",copiaTextoDos);
}

void ejemploErrorBuffer(){

	int tamMax=SIZE -1;
	char cadenaNombre[40];
	int numHermanos=0;
	char cadenaApellido[40];
	printf(" \nEjemplo error buffer \n");
	
	printf("Ingrese el numero de hermanos  \n");
	//Se define el tamanio maximo
	scanf("%d", &numHermanos);
	flush_in();
	printf("Ingrese su nombre  \n");
	//Se define el tamanio maximo
	fgets(cadenaNombre,40, stdin);
	

	printf("Ingrese su apellido  \n");
	//Se define el tamanio maximo
	fgets(cadenaApellido, 40, stdin);

	printf("Nombre: %s Apellido: %s numHermanos: %d\n", cadenaNombre,cadenaApellido,numHermanos );
	

}


/* Limpia el bufer de entrada para evitar problemas
cuando se leen cadenas*/
void flush_in() 
{ 
   int caract;

   while( (caract = fgetc(stdin)) != EOF 
   		&& caract != '\n' ){} 
}


