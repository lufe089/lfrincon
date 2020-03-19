#include <stdio.h>

typedef enum diasSemana{
	LUNES, MARTES, MIERCOLES, JUEVES, VIERNES
}dias_semana_e;

typedef enum estadoAnimo{
	CONTENTO = 1, ABURRIDO = 2, INDECISO = 3
}estado_animo_e;


void imprimirValorDiasSemana(dias_semana_e diaSemana){

	switch(diaSemana){
		case LUNES: printf("El dia es lunes \n");
					break;
		default: printf("No es lunes");
					break;
	}

	if (diaSemana == LUNES){
		printf("ES lunes");
	}
}


dias_semana_e llenarDiasSemana(){
	dias_semana_e diaUsuario;
 	printf("Ingrese numero de la semana: 0. LUNES, 1. MARTES ... \n");
 	scanf("%d", &diaUsuario);
 	return diaUsuario;
}

/* COMPLETE: mejore el codigo de llenar DiasSemanas para que le pida datos al
usuario mientras que el valor ingresado sea menor a 0 o mayor a 6 pues significaría que
no esta en el rango de los días de la semana definidos */

dias_semana_e llenarDiasSemanaMejorado(){

}

void mostrarMensajeEstadoAnimo(){

	estado_animo_e estadoAnimo = 0;
	printf("Qué estado de animo tiene: ");
	scanf("%d", &estadoAnimo);

	// Ejemplo solo con IF y valores representados como enteros
	/*if (estadoAnimo == 1) {
		printf ("Felicitaciones una actitud positiva es importante \n");
	} else if (estadoAnimo == 2){ 
		printf ("No se deprima, la vida es bella \n");
	} else if (estadoAnimo == 3){ 
		printf("Tranquilo, pongase contento \n");
	}*/

	// Ejemplo con valores del enum
	if (estadoAnimo == 	CONTENTO){
		printf ("Felicitaciones una actitud positiva es importante \n");
	}else if (estadoAnimo == ABURRIDO){ 
		printf ("No se deprima, la vida es bella \n");
	}

	// Ejemplo con valores del enum y switch case
	switch (estadoAnimo){
		case CONTENTO: printf("MENSAJE CUANDO ESTA CONTENTO \n");
						break;
		case ABURRIDO: printf("Mensaje cuando esta ABURRIDO \n");
						break;
		case INDECISO: printf("Mensaje para indecisos \n" );
						break;
	}

}

int main()
{
	// Descomente este codigo para que pueda probar las otras operaciones
	// dias_semana_t dia=llenarDiasSemana();
	// imprimirValorDiasSemana(dia);
	mostrarMensajeEstadoAnimo();
	return 0;
}