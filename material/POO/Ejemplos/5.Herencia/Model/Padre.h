#ifndef PADRE_H
#define PADRE_H

#include <iostream>
#include "Abuelo.h"

using std::cout;

class Padre : public Abuelo
{
private:
    int attPrivPadre1;

public:
    Padre();
    void imprimirMensaje();
    void metodoSoloPadre();
};

#endif // PADRE_H
