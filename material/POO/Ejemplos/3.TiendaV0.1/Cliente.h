#ifndef CLIENTE_H
#define CLIENTE_H

#include <iostream>
using std::cin;
using std::cout;
using std::endl;
using std::string;

class Cliente
{
private:
    string nombre;
    string email;
    int id;
    float cantLitrosTomados;
    string telefono;

public:
    Cliente();
    Cliente(string, string, int, string);
    void mostrarCliente();
};

#endif