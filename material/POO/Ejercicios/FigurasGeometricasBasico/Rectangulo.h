//#ifndef RECTANGULO_H
// Guardas
//#define RECTANGULO_H

#include <iostream>
#include <stdlib.h>

// Inclusion de librerias
using std::cin;
using std::cout;
using std::endl;

class Rectangulo
{
private: //Atributos
    float largo, ancho, perimetro, area;

public:           //Metodos
    Rectangulo(); //Constructor
    void calcularPerimetro();
    void calcularArea();

    // Gets and sets
    float getLargo();
    void setLargo(float largo);
    float getAncho();
    void setAncho(float ancho);
    float getPerimetro();
    float getArea();
};
//#endif /* !RECTANGULO_H */