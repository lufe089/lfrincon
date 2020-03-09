#include "Structs.h"
#include "Cadenas.h"

struct Fish llenarFishMemEstatica(){
	
	struct Fish fish;
	printf("ingrese un nombre para el pez max 24 caracteres\n");
	fgets(fish.nombre,25,stdin);
	printf("ingrese el numero de dientes \n");
	scanf("%d", &fish.numDientes);
	printf("ingrese la edad del pez\n");
	scanf("%d", &fish.edad);
	flush_in(); 
	printf("ingrese la especie para el pez max 24 caracteres\n");
	fgets(fish.especie,25,stdin);
	return fish;
}

struct Fish llenarFishTypeDef(){
	/* La lógica es igual, la diferencia es que 
	la declaración de la variable se hace con fish_t*/
	fish_t fish;
	printf("ingrese un nombre para"
		" el pez max 24 caracteres\n");
	fgets(fish.nombre,25,stdin);
	flush_in(); 
	printf("ingrese la especie para el pez max 24 caracteres\n");
	fgets(fish.especie,20,stdin);

	//TODO: Completelo para llenar todos los datos
	return fish;
}

/* Se recibe la direccion de la estructura y no su valor para impresion*/
void imprimirDatosPasoValor(fish_t fish){
	printf(".......\n......");
	printf("Nombre pez:%s \n", fish.nombre );
	printf("Especie:%s \n", fish.especie );
	//TODO: Completelo para llenar todos los datos
}