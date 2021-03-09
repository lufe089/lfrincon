#include "menu.h"

int menu()
{
    int opcion;
    std::cout << "Menu Tienda\n"
              << std::endl;
    std::cout << "1. Agregar Productos" << std::endl;
    std::cout << "2. Mostrar Productos" << std::endl;
    std::cout << "3. Agregar cliente" << std::endl;
    std::cout << "4. Mostrar clientes" << std::endl;
    std::cout << "5. Vender" << std::endl;
    std::cout << "0. Salir\n"
              << std::endl;
    std::cout << "Digita el numero: ";
    std::cin >> opcion;
    return opcion;
}