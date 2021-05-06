#ifndef FIGURA_GEOMETRICA_H
// Guardas
#define FIGURA_GEOMETRICA_H

#include <iostream>
#include <cstdlib>

using std::cin;
using std::cout;
using std::endl;
using std::string;

//CLASE FIGURA_GEOMETRICA

class FiguraGeometrica
{
private: //atributos
    string color;

protected:
    float area, perimetro;

public:
    FiguraGeometrica(); //NO OLVIDAR
    FiguraGeometrica(string color);
    virtual void calcularArea() = 0;      // Metodo virtual puro
    virtual void calcularPerimetro() = 0; // Metodo virtual puro
    virtual void mostrarFigura();
    string getColor() const;
    void setColor(string);
    float getArea() const;
    float getPerimetro() const;
};

#endif /* !FIGURA_GEOMETRICA_H */