#ifndef ABUELO_H
#define ABUELO_H

#include <iostream>

using std::cout;

class Abuelo
{
private:
    int attPrivAbuelo1;
    int attPrivAbuelo2;

protected:
    float attProtcAbuelo;

public:
    Abuelo();
    void imprimirMensaje();
    void metodoSoloAbuelo();
};
#endif // ABUELO_H
