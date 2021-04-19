#include "Rectangulo.h"

//CONSTRUCTORES RECTANGULO

Rectangulo::Rectangulo() {}

Rectangulo::Rectangulo(float ancho, float largo)
{

    this->ancho = ancho;
    this->largo = largo;
}

//METODOS RECTANGULO

void Rectangulo::calcularArea()
{
    // float area; // shadow variable -- modificando es la variable local
    this->area = this->largo * this->ancho;
}

void Rectangulo::calcularPerimetro()
{
    //float perimetro;
    this->perimetro = (2 * this->largo) + (2 * this->ancho);
}

void Rectangulo::mostrarFigura()
{
    cout << "El ancho: " << ancho << " -- "
         << "el largo: " << largo << endl;
    if (this->area == 0) // si no he calculado el area
    {
        this->calcularArea();
    }
    if (this->perimetro == 0)
    {
        this->calcularPerimetro();
    }
    cout << "El area del rectangulo es: " << this->area << endl;
    cout << "El perimetro del rectangulo es : " << perimetro << endl;

    // LLamo al mostrarFigura delegado
    FiguraGeometrica::mostrarFigura();
}

float Rectangulo::getAncho()
{
    return this->ancho;
}

float Rectangulo::getLargo()
{
    return this->largo;
}

void Rectangulo::setAncho(float ancho)
{
    this->ancho = ancho;
}
void Rectangulo::setLargo(float largo)
{
    this->largo = largo;
}
