#include <stdio.h>

int main()
{
  int a;
  int b;
  
  try {
     printf("Introduzca un número (dividendo):");
     scanf("%d", &a);
     printf("Introduzca otro número (divisor):");
     scanf("%d", &b);
     
     if ( b < -5 )
           printf("La división es %f", a/b);
     else  
      throw b;

  }
  catch(int e)
  {
     printf("Es necesario un divisor distinto de %d", e);
  }
}
