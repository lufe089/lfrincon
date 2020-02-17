
//Incluyo biblioteca de entrada/salida.
#include <stdio.h>


int funcionUno(int x, int y){
  return x+y;
}
int funcionDos(int x, int y){
  return x-y;
}
int funcionTres(int x, int y){
  return x*y;
}
float funcionCuatro(int x, int y){
  float result=0.0;
  if(y>0){
	result= (float)x/ (float)y;
  }else{
	printf("No se puede hacer esta operacion para los numeros %d--%d \n", x,y);
  }
  return result;
}

int main(){
  int a,b,c;
  float d;
  printf("Bienvenidos a este programa \n");
  printf("Ingrese el num uno \n");
  scanf("%d",&a);
  printf("Ingrese el num dos \n");
  scanf("%d",&b);
  
  //Operaciones
  c=funcionUno(a,b);
  printf("Resultado operacion uno %d \n", c);
  
   c=funcionDos(a,b);
  printf("Resultado operacion dos %d \n", c);
  
   c=funcionTres(a,b);
  printf("Resultado operacion tres %d \n", c);
  
   d=funcionCuatro(a,b);
  printf("Resultado operacion cuatro %f \n", d);
  
  return 0;

}