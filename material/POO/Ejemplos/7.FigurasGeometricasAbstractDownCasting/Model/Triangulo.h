//#ifndef TRINANGULO_H
// Guardas
//#define TRIANGULO_H

//CLASE TRIANGULO

#include <iostream>
#include <cstdlib>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

#include "FiguraGeometrica.h"

class Triangulo : public FiguraGeometrica
{
private:
    float base, altura;

public:
    Triangulo();
    Triangulo(float base, float altura);
    void calcularArea();
    void calcularPerimetro();
};

//#endif /* !TRIANGULO_H */