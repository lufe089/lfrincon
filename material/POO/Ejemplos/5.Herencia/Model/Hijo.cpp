#include "Hijo.h"

Hijo::Hijo()
    : attPrivHijo1(1000)
{
    cout << "*** Constructor hijo \n";
}

void Hijo::imprimirMensaje()
{
    cout << "Soy el hijo \n";
}

void Hijo::metodoSoloHijo()
{
    cout << "METODOSOLOHIJO: Yo como hijo defini " << attPrivHijo1 << " --"
         << "Herede de mi abuelo"
         << "--"
         << attProtcAbuelo << "\n";
}
