//#ifndef MAIN_H
// Guardas

/* Mostrar menua y validar datos de entrada */
#include "../Model/Abuelo.h"
#include "../Model/Padre.h"
#include "../Model/Hijo.h"
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class View
{
private:
public:
    int mostrarMenu();
    void verPrincipal();

    void probarPadre();

    void probarAbuelo();

    void probarHijo();

    void combinarReferencias();
};
//#define FIGURAS_CONTROLLER_H