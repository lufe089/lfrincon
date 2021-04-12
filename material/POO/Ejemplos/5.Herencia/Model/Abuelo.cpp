#include "Abuelo.h"

Abuelo::Abuelo()
    : attPrivAbuelo1(100),
      attPrivAbuelo2(101),
      attProtcAbuelo(200)
{
    cout << "*** Constructor abuelo \n";
}

void Abuelo::imprimirMensaje()
{
    cout << "ImprimirMensaje: Soy el abuelo \n";
}

void Abuelo::metodoSoloAbuelo()
{
    cout << "Solo abuelo: Yo como abuelo defini " << attPrivAbuelo1 << "--"
         << attPrivAbuelo2 << "--"
         << attProtcAbuelo << "\n";
}
