//
// Created by lufe0 on 7/05/2021.
//

#ifndef CASINO_JUGADOR_H
#define CASINO_JUGADOR_H
#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

enum ESTADO_JUGADOR{
    /* Por retirar cuando no tiene dinero para comprar mas gonzos */
    ACTIVO, SIN_GONZOS, POR_RETIRAR, RETIRADO
};


class Jugador
{
private: //atributos
    string nombre;
    long id;

private:
    float cantGonzos;
    int cantJuegos;

public:
    Jugador();
    Jugador(long id, string nombre, float cantGonzos);
    ~Jugador(); // Destructor
    void aumentarJuegos();
    void mostrarInfo(); // Presenta información del diner, los gonzos, cantidad de juegos ganados y perdidos
    void actualizarGonzos(float resultadoJuego);
    long getId() const;
    const string &getNombre() const;
    float getCantGonzos() const;
    int getCantJuegos() const;
};
#endif //CASINO_JUGADOR_H
