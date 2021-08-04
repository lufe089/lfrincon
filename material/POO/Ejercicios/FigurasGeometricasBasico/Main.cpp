/*Ejercicio 1: Este programa tiene una clase llamada Rectangulo que tenga los siguientes
atributos: largo y ancho, y los siguientes metodos: calcularPerimetro() y calcularArea()
Modificado de Curso de programación en c++ .

Agregue un nuevo metodo privado llamado "mostrarFigura", este metodo debe mostrar el ancho,
largo, area y perimetro de la figura. Si el area y el perimetro estan en cero,
entonces el método debe primero llamar a los metodos para calcular area y perimetro. 


Canal programación ATS
*/

#include "Rectangulo.h"

void probarRectangulos()
{
    float alto;
    float ancho;

    cout << "Ingrese el alto del rectangulo uno \n";
    cin >> alto;

    cout << "Ingrese el ancho del rectangulo uno \n";
    cin >> ancho;

    // Crear el objeto
    Rectangulo rectanguloUno;

    // Poner los valores
    rectanguloUno.setLargo(alto);
    rectanguloUno.setAncho(ancho);

    // Calcular y mostrar area
    rectanguloUno.calcularArea();
    cout << "El area es: "
         << rectanguloUno.getArea() << "\n";

    //  To-DO: Probar lo mismo con el rectangulo dos
}

int main()
{
    probarRectangulos();
    system("pause");
    return 0;
}
