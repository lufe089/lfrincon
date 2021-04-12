#ifndef HIJO_H
#define HIJO_H

#include <iostream>
#include "Padre.h"

using std::cout;

class Hijo : public Padre
{
private:
    int attPrivHijo1;

public:
    Hijo();
    void imprimirMensaje();
    void metodoSoloHijo();
};

#endif // HIJO_H
