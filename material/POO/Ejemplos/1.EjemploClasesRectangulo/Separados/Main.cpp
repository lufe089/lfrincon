/*Ejercicio 1: Construya una clase llamada Rectangulo que tenga los siguientes
atributos: largo y ancho, y los siguientes metodos: perimetro() y area()
Modificado de Curso de programación en c++ 
Canal programación ATS
*/

#include <iostream>
#include <stdlib.h>
#include "Rectangulo.h"

int main()
{
    Rectangulo rectangulo(11, 7);

    rectangulo.calcularPerimetro();
    rectangulo.calcularArea();

    Rectangulo rectangulo2(10, 20);
    rectangulo2.calcularPerimetro();

    system("pause");
    return 0;
}
