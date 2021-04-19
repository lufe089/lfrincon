//#ifndef CIRCULO_H
// Guardas
//#define CIRCULO_H

#include <iostream>
#include <cstdlib>

using std::cin;
using std::cout;
using std::endl;

#include "FiguraGeometrica.h"

//CLASE CIRCULO

class Circulo : public FiguraGeometrica
{
private: //atributos
    float radio;
    const static float PI;

public:
    Circulo(); //NO OLVIDAR
    Circulo(float);
    virtual void calcularArea() override;
    virtual void calcularPerimetro() override;
    virtual void mostrarFigura();
    float getRadio() const;
    void setRadio(float);
};

//#endif /* !CIRCULO_H */