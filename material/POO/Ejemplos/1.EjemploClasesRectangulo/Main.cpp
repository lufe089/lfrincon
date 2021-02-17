/*Ejercicio 1: Construya una clase llamada Rectangulo que tenga los siguientes
atributos: largo y ancho, y los siguientes metodos: perimetro() y area()
Modificado de Curso de programación en c++ 
Canal programación ATS
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

class Rectangulo
{
private: //Atributos
    float largo, ancho;

public:                       //Metodos
    Rectangulo(float, float); //Constructor
    void calcularPerimetro();
    void calcularArea();
};

Rectangulo::Rectangulo(float largo, float ancho)
{
    this->largo = largo;
    this->ancho = ancho;
}

void Rectangulo::calcularPerimetro()
{
    float perimetro;

    perimetro = (2 * largo) + (2 * ancho);

    cout << "El perimetro es: " << perimetro << endl;
}

void Rectangulo::calcularArea()
{
    float area;

    area = largo * ancho;

    cout << "El area es: " << area << endl;
}

int main()
{
    Rectangulo rectangulo(11, 7);

    rectangulo.calcularPerimetro();
    rectangulo.calcularArea();

    system("pause");
    return 0;
}
