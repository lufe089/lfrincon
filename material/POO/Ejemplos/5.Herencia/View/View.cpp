#include "View.h"

//FUNCIONES DEL PROGRAMA

void View ::combinarReferencias()
{
    // Objeto derivado asignado a objeto de tipo padre
    Abuelo abueloObj;
    Padre padreObj;
    Hijo hijoObj;

    // Apuntadores
    Padre *pPadre;
    Hijo *pHijo;

    pPadre = &hijoObj;
    pPadre->imprimirMensaje(); // Funciona pero llama la del padre

    // NO funciona-> solo se pueden acceder a métodos
    // de la misma referencia
    // pPadre = &hijoObj;
    // pPadre->probarHijo();

    // Objeto padre asignado a objeto de tipo hijo
    /* Error: a value of type "Abuelo *" cannot be used 
    to initialize an entity of type "Hijo *"C/C++(144) */
    // pHijo = padreObj;
}
void View::probarHijo()
{
    // Crear objeto de tipo padre
    Hijo hijo;
    cout << "Metodo del abuelo llamado desde el hijo por herencia \n";
    hijo.metodoSoloAbuelo();
    hijo.metodoSoloHijo();
}

void View::probarPadre()
{
    // Crear objeto de tipo padre
    Padre padre;
    cout << "Metodo del abuelo llamado desde el padre por herencia \n";
    padre.metodoSoloAbuelo();
}

void View::probarAbuelo()
{
    // Crear objeto de tipo abuelo
    Abuelo abuelo;
    // LLamar metodos abuelo
    abuelo.imprimirMensaje();
    abuelo.metodoSoloAbuelo();
}

int View::mostrarMenu()
{
    int opcion;
    cout << "Menu\n"
         << std::endl;
    cout << "1. Probar abuelo" << std::endl;
    cout << "2. Probar padre" << std::endl;
    cout << "3. Probar hijo" << std::endl;
    cout << "4. Pruebas combinadas combinado" << std::endl;
    cout << "0. Salir\n"
         << std::endl;
    cout << "Digita el numero: ";
    cin >> opcion;
    return opcion;
}

void View::verPrincipal()
{
    int opcion;
    do
    {
        opcion = mostrarMenu();
        switch (opcion)
        {
        case 1:
            probarAbuelo();
            break;
        case 2:
            probarPadre();
            break;
        case 3:
            probarHijo();
            break;
        case 4:
            combinarReferencias();
            break;
        }
    } while (opcion != 0);
}