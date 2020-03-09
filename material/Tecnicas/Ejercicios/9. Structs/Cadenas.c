#include "Cadenas.h"
#include <stdio.h>
/* Limpia el bufer de entrada para evitar problemas
cuando se leen cadenas*/
void flush_in() 
{ 
   int caract;

   while( (caract = fgetc(stdin)) != EOF 
   		&& caract != '\n' ){} 
}


