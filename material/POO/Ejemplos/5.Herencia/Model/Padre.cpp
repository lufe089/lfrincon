#include "Padre.h"

Padre::Padre()
    : Abuelo(),
      attPrivPadre1(20)
{
    cout << "*** Constructor padre \n";
}

void Padre::imprimirMensaje()
{
    cout << "Soy el padre \n";
}

void Padre::metodoSoloPadre()
{
    cout << "Yo como padre defini " << attPrivPadre1 << "\n"
         << "Herede"
         << "\n"
         << attProtcAbuelo;
}
