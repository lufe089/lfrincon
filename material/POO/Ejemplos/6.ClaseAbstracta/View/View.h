//#ifndef MAIN_H
// Guardas

/* Mostrar menua y validar datos de entrada */
#include "../Controller/FigurasController.h"
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

class View
{
private:
    // Objeto de tipo FigurasController para enlazar la logica
    FigurasController controller;

public:
    void pedirDatosRectangulo();
    void pedirDatosCirculo();
    void pedirDatosTriangulo();
    void mostrarRectangulos();
    void mostrarCirculos();
    void mostrarTriangulos();
    void mostrarTodos();
    int mostrarMenu();
    void verPrincipal();
};
//#define FIGURAS_CONTROLLER_H