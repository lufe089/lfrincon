#include <iostream>
#include "tienda.h"
#include "producto.h"
#include "menu.h"

int main()
{
    Tienda laFarra;
    int opcion, i;
    std::cout << "\n";
    do
    {
        opcion = menu();
        switch (opcion)
        {
        case 0:
            break;
        case 1:
            laFarra.agregarProducto();
            break;
        case 2:
            std::cout << "\n";
            laFarra.mostrarTodosProducto();
            std::cout << "\n";
            break;
        case 3:
            std::cout << "Lo siento no esta hecha \n";
            break;
        case 4:
            laFarra.mostrarTodosCliente();
        default:
            std::cout << "\nNumero invalido\n"
                      << std::endl;
            break;
        }
    } while (opcion != 0);
    return 0;
}