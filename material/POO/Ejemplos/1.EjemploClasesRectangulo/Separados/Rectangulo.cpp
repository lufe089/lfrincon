#include <iostream>
#include "Rectangulo.h"

using namespace std;

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
